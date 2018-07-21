# Execute Get informatin from switch and wil into csv File/ Tim Waldesbuehl (avzwat)
# Created: 21.07.2018, Last Updated: 21.07.2018

switch_output_list = []
switch_output_file = open('switch_ouput.txt', 'r')
for i in switch_output_file:
    switch_output_list.append(i)
switch_output_file.close()

del switch_output_list[0]

for i in switch_output_list:
    i = ''.join(i)
    print(i)
