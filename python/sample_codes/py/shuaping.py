# shuaping  shuaping  shuaping  shuaping  shuaping  shuaping
def main():
    x=1
    y=1
    z=0
    for i in range(20):
        for i in range(50):
            print x
            y=(y+1)%10
            x=x*10+y
        print x
        print x
        for i in range(50):
            print x
            z=x%10
            x=(x-z)/10
    print x
    z=raw_input('...')
main()
