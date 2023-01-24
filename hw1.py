import module1, module3, module4

gr = module4.Group('Python-pro')

st1 = module3.Student('Kuzmenko', 'Ivan', '19')
st2 = module3.Student('Tkachenko', 'Ivan', '29')
st3 = module3.Student('Levchenko', 'Ivan', '39')
st4 = module3.Student('Shevchenko', 'Ivan', '88')
st5 = module3.Student('Kravchenko', 'Ivan', '18')
st6 = module3.Student('Serhienko', 'Ivan', '28')
st7 = module3.Student('Petrenko', 'Ivan', '48')
st8 = module3.Student('Maksymenko', 'Ivan', '23')
st9 = module3.Student('Ivanenko', 'Ivan', '17')
st10 = module3.Student('Borysenko', 'Ivan', '35')
st11 = module3.Student('Brovko', 'Ivan', '35')
st12 = module3.Student('Rudnko', 'Ivan', '55')

try:
    gr.add_st(st1)
    gr.add_st(st2)
    gr.add_st(st3)
    gr.add_st(st4)
    gr.add_st(st5)
    gr.add_st(st6)
    gr.add_st(st7)
    gr.add_st(st8)
    gr.add_st(st9)
    gr.add_st(st10)
    gr.add_st(st11)
    gr.add_st(st12)
except module1.LimitError as error:
    print(error)

print(gr)
# surname = input('Enter surname: ')
# a = gr.search_st(surname)
# print('*'.join(map(str, a)))