import module_Student
import module_logging, module_Human, module_Group

gr = module_Group.Group('Python-pro')

st1 = module_Student.Student('Kuzmenko', 'Ivan', '19')
st2 = module_Student.Student('Tkachenko', 'Ivan', '29')
st3 = module_Student.Student('Levchenko', 'Ivan', '39')
st4 = module_Student.Student('Shevchenko', 'Ivan', '88')
st5 = module_Student.Student('Kravchenko', 'Ivan', '18')
st6 = module_Student.Student('Serhienko', 'Ivan', '28')
st7 = module_Student.Student('Petrenko', 'Ivan', '48')
st8 = module_Student.Student('Maksymenko', 'Ivan', '23')
st9 = module_Student.Student('Ivanenko', 'Ivan', '17')
st10 = module_Student.Student('Borysenko', 'Ivan', '35')
st11 = module_Student.Student('Brovko', 'Ivan', '35')
st12 = module_Student.Student('Rudnko', 'Ivan', '55')

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
except module_logging.LimitError as error:
    print(error)

print(gr)
# surname = input('Enter surname: ')
# a = gr.search_st(surname)
# print('*'.join(map(str, a)))