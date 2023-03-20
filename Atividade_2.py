def main():
    #solicitando ao usuario o numero que o mesmo deseja informar e guardando o valor na variavel number
    number = int(input("Informe o numero desejado: "))
    I1 = 0
    I2 = 1
    I3 = 0
    n = 20
    sequence_fibonacci = []
    sequence_element = []

    #criando a sequencia de fibonacci e anexando a mesma em um array
    for i in range(n-1):
        if (i%2)==0:
            I1 = I3

        if (i%2)==1:
            I2 = I3

        I3 = I1 + I2

        sequence_fibonacci.append(I3)
    
    #percorrendo o array de fibonacci e extraindo o elemento igual ao numero informado pelo usuario
    for j in range(len(sequence_fibonacci)):
        if(number == sequence_fibonacci[j] ):
            sequence_element = sequence_fibonacci[j]

    #criando as condicoes necessarias para informar se o numero pertence ou nao a sequencia de fibonacci
    if(number == sequence_element):
        print("Este numero pertence a sequencia de fibonacci!")
    else:
        print("Este numero nao pertence a sequencia de fibonacci!")
        
#chamando a funcao main para exbir os resultados
main()