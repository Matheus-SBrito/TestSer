from modulos.professor.profesor_dao import buscar_professores

def validar_log_professor (matricula, senha):
    
    usuario_encontrado = buscar_professores(matricula)
    
    if not usuario_encontrado:
        raise Exception ("Usuario não Encontrado")
    
    if usuario_encontrado.get_senha() != senha:
        raise Exception ("Senha Incorreta")
    
    return True
    