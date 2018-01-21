
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions
# with denominators 2 to 10 are given:
#
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that
# 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
# its decimal fraction part.
def sequence(n):
    remainder = 1%n
    q = ''
    rem_list = []
    while True:
        rem_list.append(remainder)
        remainder = remainder*10
        q += str(remainder//n)
        remainder = remainder%n
        if remainder in rem_list :
            i = rem_list.index(remainder)
            return q[i:]

def main(limit):
    max_length = 0
    num = 0
    for i in range(2,limit):
        temp = len(sequence(i))
        if temp > max_length :
            max_length = temp
            num = i
    print('d:{},digits:{}'.format(num,max_length))

if __name__=='__main__':
    main(1000)





