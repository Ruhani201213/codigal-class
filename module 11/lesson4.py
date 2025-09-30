class subway:

    def __init__(self):
        print('subway created')

    def __del__(self):
        print('destrutor called,subway deleted')

obj=subway()
del obj