import argparse

variable = {}
fonction = {}#"test" : ([nom_variable],line debut , line fin)
class Type:
    def __init__(self,keyword,baseValue):
        self.keyword = keyword
        self.baseValue = baseValue
class variables:
    def __init__(self,_type:Type,value,scope):
        self.type = _type
        self.value =value
        self.scope = scope

entier = Type("ENTIER",0)
booleen = Type("BOOLEEN","faux")
decimal = Type("DECIMAL","0,0")
text = Type("TEXT","")
type_list = [entier,booleen,decimal,text]

code_stack = [("entry point",0)]
FONC_list  = []

def eval(file):
    global variable
    lines = file.split(".")
    program_compter = 0
    lines = [x for x in lines if x != ""]#supprimer les espace vide

    while program_compter < len(lines):
        line = lines[program_compter]
        #if line.startswith("//"):
        #    continue
        program_compter = eval_line(line,program_compter,lines)
    #for i in variable:
    #    print(f"{i} , {variable.get(i).type.keyword} , {variable.get(i).value} , {variable.get(i).scope}")
    #print(FONC_list)
def scan_program(lines,line_end,get):
    stack = []
    last_get = 0
    for i in range(line_end):
        keyword = lines[i].split()[0]
        keyword.replace(" ","")
        keyword = keyword.replace('\xa0', '')
        if keyword == "REPETER": stack.append(("REPETER",i))
        if keyword == "FONCTION": stack.append(("FONCTION", i))
        if keyword == "SI": stack.append(("SI", i))
        if keyword == "FIN" :
            stack.pop()
    value = ("NULL",0)
    while value[0] != get:
        if len(stack) > 0:
            value = stack.pop()
        else:
            break
    return  value[1] # retourne le dernier block de type get ou l'utilisateur et dedans utils pour stop qui dois recuperer le dernier repeter
def scan_end(lines,line_bloc):
    stack = []
    for i in range(len(lines)):
        keyword = lines[i].split()[0]
        if keyword == "REPETER": stack.append(("REPETER", i))
        if keyword == "SI": stack.append(("SI", i))
        if keyword == "FONCTION": stack.append(("FONCTION", i))
        if keyword == "FIN" or keyword == "SINON":
            value = stack.pop()
            if value[1] == line_bloc and (value[0] == "SI" or keyword == "FIN"):
                return i , keyword #retourn l'addresse de FIN du block specifier (pour les si)
        if keyword == "SINON": stack.append(("SINON", i))#ajoute comme un arg si ce n'est pas celuis du retour

def eval_line(line:str,pro:int,program):
    global variable,type_list
    line = line.lstrip()
    line = line.replace(":", " :")
    keyword = ["VARIABLE","METTRE","AFFICHER","REPETER","FIN","STOP","SI","IMPRIMER","SINON","FONCTION"]
    line_split = line.split()
    keyword_use = line_split[0]
    if keyword_use in keyword:
        match keyword_use:
            case "VARIABLE":
                _Type = entier
                for e in type_list:
                    if e.keyword == line_split[3]:
                        _Type = e
                if line_split[2] != "TYPE":
                    raise TypeError(f"Une variable est definis sans TYPE , {line}")
                variable[line_split[1]] = variables(_Type,_Type.baseValue,code_stack[:])
            case "METTRE":
                if line_split[2] != "Ã":
                    raise TypeError(f"METTRE doit avoir un à , {line}")
                expr = line[len(f"{line_split[0]} {line_split[1]} à"):]
                value , type = eval_expr(expr)
                value = bool_replace(type,value)
                variable.get(get_var(line_split[1],code_stack)).value = value
            case "AFFICHER":
                expr = line[len(f"{line_split[0]}"):]
                variable_afficher , type = eval_expr(expr)
                variable_afficher = bool_replace(type,variable_afficher)
                print(variable_afficher)
            case "IMPRIMER":
                expr = line[len(f"{line_split[0]}"):]
                variable_afficher, type = eval_expr(expr)
                variable_afficher = bool_replace(type, variable_afficher)
                print(variable_afficher,end="")
            case "REPETER":
                code_stack.append(("rep",pro))
            case "FIN":
                value , line = code_stack.pop()
                if value == "rep":
                    return line
            case "SINON":
                code_stack.append(("SINON",pro))
                if not scan_end(program,pro):
                    raise TypeError("pas de fin d'un sinon")
            case "STOP":
                last_repeter = scan_program(program,pro,"REPETER")
                jmp_to = scan_end(program,last_repeter)[0]
                value , line = (None,None)
                while not value == "rep":
                    value , line = code_stack.pop()#enleve tout les fonction jusqu'aux repeter le plus proche

                return jmp_to + 1
            case "SI":
                code_stack.append(("si", pro))
                expr = line[len(f"{line_split[0]}"):][:-5]
                value , type = eval_expr(expr)
                value = bool_replace(type, value)
                if value != "VRAIS":
                    jmp_to , keyword = scan_end(program,pro)
                    return jmp_to
            case "FONCTION":
                name = line_split[1]
                is_in_func = code_stack[len(code_stack) - 1][0] == name
                if is_in_func:
                    variables_str = line[len(f"{line_split[0]} {name}, :"):]
                    variables_str_list = variables_str.split()
                    num_var = int(len(variables_str_list)/3)
                    for i in range(num_var):
                        var = i * 3
                        _name = variables_str_list[var]
                        _TYPE_keyword = variables_str_list[var + 1]
                        _TYPE = variables_str_list[var + 2]
                        _Type = entier
                        for e in type_list:
                            if e.keyword == _TYPE:
                                _Type = e
                        variable[_name] = variables(_Type,_Type.baseValue,code_stack[:])
                else:
                    FONC_list.append((name,pro))
                    jmp_to, keyword = scan_end(program, pro)
                    return jmp_to + 1
    return  pro + 1
def bool_replace(type,value):
    if type == "bool":
        match value:
            case 0:
                value = "FAUX"
            case 1:
                value = "VRAIS"
    return value

def get_var(name,scope):
    try:
        var = variable[name]
        var_scope = var.scope[len(var.scope) - 1]#recupere le dernier element de la liste
        if var_scope in scope:
            return name
        else:
            raise TypeError(f"varaible non defini dans le scope actuelle , {scope}")
    except:
        raise TypeError("varaible non defini")


def replace_notSring(expr):
    stack = []
    result = []

    for e in expr:
        if e == "<": stack.append(0)
        elif e == ">":stack.pop()
        if e == " " and len(stack) == 0: continue
        result.append(e)

    return "".join(result)
def eval_expr(expr : str):
    is_parentise = []
    expr = replace_notSring(expr)
    expr = expr.replace('\xa0', '')
    expr = expr.replace("COMME", " COMME ")
    if expr.startswith("(") and expr.endswith(")"):
        expr = expr[1:]
        expr = expr[:-1]
    operation = ["+",'-',"*","/","=","!"]
    bool_value = ["FAUX","VRAIS"]
    do_op = ""
    expr_left = None
    expr_right = None
    i = 0
    is_COMME_operation = False
    for char in expr:
        is_COMME_operation = False
        if char == "(" or char == "<":
            is_parentise.append(True)
        if char == ")" or char == ">":
            is_parentise.pop()
        is_COMME_operation = (char == "C" and expr[i+1] == "O"
        and expr[i+2] == "M" and expr[i+3] == "M" and expr[i+4] == "E")#un petite code Trés lisible qui verifie SI COMME est utiliser
        if is_COMME_operation and not len(is_parentise) > 0:
            do_op = "COMME"
            expr_left = expr[:i]
            expr_right = expr[i+4:]
            expr_right = expr_right[1:]
            break
        if char in operation and not len(is_parentise) > 0:
            do_op = char
            expr_left = expr[:i]
            expr_right = expr[i:]
            expr_right = expr_right[1:]
            break
        i += 1
    if not expr_left == None:
        if not do_op == "!" : value_left , type_left = eval_expr(expr_left)
        else : value_left = 0 ; type_left = "bool"
        value_right , type_right = eval_expr(expr_right)

        if type_right == "Type":
            if type_left == "int":
                if do_op == "COMME":
                    if value_right == "TEXT": return str(value_left), "str"
                    if value_right == "BOOLEEN": return int(value_left > 0), "bool"
                else:
                    raise TypeError("undefined type")
            if type_left == "bool":
                if do_op == "COMME":
                    if value_right == "ENTIER": return value_left, "int"
                else:
                    raise TypeError("undefined type")
            if type_left == "str":
                if do_op == "COMME":
                    if value_right == "ENTIER": return int(value_left), "int"
                else:
                    raise TypeError("undefined type")
        if type_left == type_right:
            if type_left == "int":
                if do_op == "+":return value_left + value_right , "int"
                if do_op == "-":return value_left - value_right , "int"
                if do_op == "*":return value_left * value_right , "int"
                if do_op == "/":return value_left / value_right , "int"
                if do_op == "=":return int(value_left == value_right) , "bool"
            if type_left == "str":
                if do_op == "+":return value_left + value_right , "str"
                if do_op == "=": return int(value_left == value_right), "bool"
            if type_left == "bool":
                if do_op == "!": return 1 - value_right , "bool"
    else:

        if expr in variable :
            _variable = variable[get_var(expr,code_stack)]
            if _variable.type.keyword == "ENTIER" : return _variable.value , "int"
            if _variable.type.keyword == "BOOLEEN":
                match _variable.value:
                    case "FAUX":return 0 , "bool"
                    case "VRAIS":return 1 , "bool"

            if _variable.type.keyword == "TEXT": return _variable.value, "str"
        elif expr in bool_value and expr == "VRAIS": return 1 , "bool"
        elif expr in bool_value and expr: return 0 , "bool"
        elif expr.startswith("<") and expr.endswith(">") : return expr[1:][:-1] , "str"
        elif "TEXT" in expr: return "TEXT" , "Type"
        elif "BOOLEEN" in expr: return "BOOLEEN", "Type"
        elif "ENTIER" in expr: return "ENTIER", "Type"
        elif "ENTRER" in expr: return input(), "str"
        elif not expr in bool_value: return int(expr), "int"
        else: raise TypeError("wrong type")


def open_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        line = ""
        for i in lines : line += i
        return line.replace("\n" , "")

parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()

file = open_file(args.filename)

eval(file)