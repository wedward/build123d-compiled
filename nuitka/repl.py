from build123d import *

env = globals().copy()
env.update(locals())


def main():

    print('WELCOME TO THE BUILD123D REPL\n\n')

    while True:

    ## READ
        uip = input('> ')

        match uip:
            case 'exit':
                break
            case _:
                
    ## EVAL
                try:
                    result =   exec( uip, env, env )
                except Exception as e:
                    print(f"FAIL: {e}")
                    result = None
    ## PRINT
                if result is not None:
                    print(result)
                
                print()

    ## LOOP 


    ## END REPL
    print('goodbye')



if __name__ == "__main__":
    main()