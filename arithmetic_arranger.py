import operator

ops = {'+':operator.add, '-':operator.sub}

a_lst = []
sep_lst = []
b_lst = []
sol_lst = []
first_line = ''
second_line = ''
sep_line = ''
sol_line = ''


def arithmetic_arranger(problems, show_sol=False):

    if len(problems) > 5:
        error = 'Error: Too many problems.'
        return error

    for problem in problems:
        sep = problem.split()
        a = sep[0]
        op = sep[1]
        b = sep[2]

        if op=='+' or op=='-':
            pass
        else:
            error = 'Error: Operator must be "+" or "-".'
            return error

        if a.isdigit() and b.isdigit():
            pass
        else:
            error = 'Error: Numbers must only contain digits.'
            return error

        if len(a)<5 and len(b)<5:
            pass
        else:
            error = 'Error: Numbers cannot be more than four digits.'
            return error


        sol = ops[op](int(a),int(b))

        op_len = max(len(a),len(b)) + 2

        a_lst.append(a.rjust(op_len,' '))
        b_lst.append(op+b.rjust(op_len-1,' '))
        sep_lst.append('-'*op_len)
        sol_lst.append(str(sol).rjust(op_len,' '))

    first_line = '   '.join([item for item in a_lst])
    second_line = '   '.join([item for item in b_lst])
    sep_line = '   '.join([item for item in sep_lst])
    sol_line = '   '.join([item for item in sol_lst])

    output_list = [first_line, second_line, sep_line, sol_line]


    if show_sol==True:
        answer = '\n'.join(output_list)
        return answer
    else:
        del output_list[-1]
        answer = '\n'.join(output_list)
        return answer


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "345 + 567"]))