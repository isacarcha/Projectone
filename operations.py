def main(input_filename,output_filename):
    with open(input_filename,'r') as input_file,\
         open(output_filename,'w')as output_file:
        for line in input_file:
            if len(line)>0:
                line=line.split()
                output_file.write('(0)\n'.format(operate(line(0))))

#hola soy isabel esto es
#una prueba

def operate(x,y):
    return int(x)+int(y)

if __name__=='__main__':
    main('number.in','numbers.out')
