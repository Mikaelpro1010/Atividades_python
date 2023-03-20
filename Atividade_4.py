def main():
    SP = 67836.43 
    RJ = 36678.66 
    MG = 29229.88
    ES = 27165.48
    Outros = 19849.53
    total_mensal = 180759.98

    #calculando a porcentagem de SP
    porcentagem_SP = SP * 100 / total_mensal
        
    #calculando a porcentagem de RJ
    porcentagem_RJ = RJ * 100 / total_mensal 

    #calculando a porcentagem de MG
    porcentagem_MG = MG * 100 / total_mensal

    #calculando a porcentagem de ES
    porcentagem_ES = ES * 100 / total_mensal
        
    #calculando a porcentagem de Outros
    porcentagem_Outros = Outros * 100 / total_mensal

    print("O percentual de representacao de cada estado foi:\n SP: %.2f por cento;\n RJ: %.2f por cento;\n MG: %.2f por cento;\n ES: %.2f por cento;\n Outros: %.2f por cento" %(porcentagem_SP, porcentagem_RJ, porcentagem_MG, porcentagem_ES, porcentagem_Outros))

#chamando a funcao principal
main()