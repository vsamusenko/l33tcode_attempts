class Category:
    def __init__(self, cat_name):
        self.ledger = []
        self.cat_name = str(cat_name).lower().capitalize()
        self.funds = 0.0

    def check_funds(self,ch_amount):
        self.ch_amount = float(ch_amount)
        if self.ch_amount > self.funds:
            return False
        else:
            return True

    def deposit(self, dep_amount, dep_desc=''):
        self.dep_amount = '%.2f' % float(dep_amount)
        self.dep_desc = dep_desc
        self.funds += float(dep_amount)
        self.ledger.append({'amount': self.dep_amount,
                            'description': str(self.dep_desc)})

    def withdraw(self, w_amount, w_desc=''):
        self.w_amount = '%.2f' % float(w_amount)
        self.w_desc = w_desc
        if self.check_funds(w_amount) :
            self.funds -= float(w_amount)
            self.ledger.append({'amount': '-' + self.w_amount,
                                'description': str(self.w_desc)})
            return True
        else:
            return False

    def get_balance(self):
        return self.funds

    def transfer(self, t_amount, t_destcat):
        self.t_amount = '%.2f' % float(t_amount)

        if isinstance(t_destcat, Category):
            if self.check_funds(t_amount) :
                self.funds -= float(t_amount)
                t_destcat.funds += float(t_amount)
                self.ledger.append({'amount': '-' + self.t_amount,
                                    'description': 'Transfer to ' + t_destcat.cat_name})
                t_destcat.ledger.append({'amount': self.t_amount,
                                         'description': 'Transfer from ' + self.cat_name})
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        print(self.cat_name.center(30,'*'))
        for line in self.ledger:
            print(line['description'][:23].ljust(23,' ') + line['amount'][:7].rjust(7, ' '))
        return 'Total: ' + ('%.2f' % self.funds)


def create_spend_chart(list_of_cat):
    spent_list = []
    spent_perc_list = []
    spent_summ = 0.0
    table_perc = [100,90,80,70,60,50,40,30,20,10,0]
    output_str = 'Percentage spent by category'
    sepline = '    ' + '---' * len(list_of_cat)
    max_len = 0

    for cat in list_of_cat:
        spent_in_cat = 0.0
        for line in cat.ledger:
            if float(line['amount']) < 0:
                spent_in_cat += abs(float(line['amount']))

        spent_list.append(spent_in_cat)

    for summ in spent_list:
        spent_summ += summ

    for summ in spent_list:
        try:
            perc_of_total = (round((summ / (spent_summ/100))/10))*10
            spent_perc_list.append(perc_of_total)
        except:
            spent_perc_list.append(0)

    for line in table_perc:
        bar_line_str = f'{str(line)}|'.rjust(4,' ')
        for cat in spent_perc_list:
            if cat >= line :
                bar_line_str += 'o'.center(3,' ')
            else:
                bar_line_str += ' '.center(3,' ')

        output_str += '\n' + bar_line_str

    output_str += '\n' + sepline

    for cat in list_of_cat:
        if len(cat.cat_name) > max_len:
            max_len = len(cat.cat_name)



    for letter in range(max_len):
        name_line_str = ''

        for cat in list_of_cat:
            try:
                name_line_str += cat.cat_name[letter].center(3, ' ')
            except:
                name_line_str += ' '.center(3, ' ')

        output_str += '\n' + '    ' + name_line_str

    return output_str


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

