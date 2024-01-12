import time
import random

def main():
    print(help)
    ai = input("Type 'help'\n")
    
    if ai == "help":
        print("GNU bash, version 5.0.17(1)-release (x86_64-pc-linux-gnu)\nThese shell commands are defined internally.  Type `help' to see this list.\nType `help name' to find out more about the function `name'.\nUse `info bash' to find out more about the shell in general.\nUse `man -k' or `info' to find out more about commands not in this list.\n\nA star (*) next to a name means that the command is disabled.\n\n job_spec [&]                                                 history [-c] [-d offset] [n] or history -anrw [filename] >\n (( expression ))                                             if COMMANDS; then COMMANDS; [ elif COMMANDS; then COMMAND>\n . filename [arguments]                                       jobs [-lnprs] [jobspec ...] or jobs -x command [args]\n :                                                            kill [-s sigspec | -n signum | -sigspec] pid | jobspec ..>\n [ arg... ]                                                   let arg [arg ...]\n [[ expression ]]                                             local [option] name[=value] ...\n alias [-p] [name[=value] ... ]                               logout [n]\n bg [job_spec ...]                                            mapfile [-d delim] [-n count] [-O origin] [-s count] [-t]>\n bind [-lpsvPSVX] [-m keymap] [-f filename] [-q name] [-u n>  popd [-n] [+N | -N]\n break [n]                                                    printf [-v var] format [arguments]\n builtin [shell-builtin [arg ...]]                            pushd [-n] [+N | -N | dir]\n caller [expr]                                                pwd [-LP]\n case WORD in [PATTERN [| PATTERN]...) COMMANDS ;;]... esa>   read [-ers] [-a array] [-d delim] [-i text] [-n nchars] [>\n cd [-L|[-P [-e]] [-@]] [dir]                                 readarray [-d delim] [-n count] [-O origin] [-s count] [->\n command [-pVv] command [arg ...]                             readonly [-aAf] [name[=value] ...] or readonly -p\n compgen [-abcdefgjksuv] [-o option] [-A action] [-G globpa>  return [n]\n complete [-abcdefgjksuv] [-pr] [-DEI] [-o option] [-A acti>  select NAME [in WORDS ... ;] do COMMANDS; done\n compopt [-o|+o option] [-DEI] [name ...]                     set [-abefhkmnptuvxBCHP] [-o option-name] [--] [arg ...]\n continue [n]                                                 shift [n]\n coproc [NAME] command [redirections]                         shopt [-pqsu] [-o] [optname ...]\n declare [-aAfFgilnrtux] [-p] [name[=value] ...]              source filename [arguments]\n dirs [-clpv] [+N] [-N]                                       suspend [-f]\n disown [-h] [-ar] [jobspec ... | pid ...]                    test [expr]\n echo [-neE] [arg ...]                                        time [-p] pipeline\n enable [-a] [-dnps] [-f filename] [name ...]                 times\n eval [arg ...]                                               trap [-lp] [[arg] signal_spec ...]\n exec [-cl] [-a name] [command [arguments ...]] [redirectio>  true\n exit [n]                                                     type [-afptP] name [name ...]\n export [-fn] [name[=value] ...] or export -p                 typeset [-aAfFgilnrtux] [-p] name[=value] ...\n false                                                        ulimit [-SHabcdefiklmnpqrstuvxPT] [limit]\n fc [-e ename] [-lnr] [first] [last] or fc -s [pat=rep] [co>  umask [-p] [-S] [mode]\n fg [job_spec]                                                unalias [-a] name [name ...]\n for NAME [in WORDS ... ] ; do COMMANDS; done                 unset [-f] [-v] [-n] [name ...]\n for (( exp1; exp2; exp3 )); do COMMANDS; done                until COMMANDS; do COMMANDS; done\n function name { COMMANDS ; } or name () { COMMANDS ; }       variables - Names and meanings of some shell variables\n getopts optstring name [arg]                                 wait [-fn] [id ...]\n hash [-lr] [-p pathname] [-dt] [name ...]                    while COMMANDS; do COMMANDS; done\n help [-dms] [pattern ...]                                    { COMMANDS ; }")
        time.sleep(1)
        print("\n")
        time.sleep(1)
        print("\n")
        time.sleep(1)
        main()
    
    elif ai == "no":
        quit()
        
    elif ai == " ":
        try:
            ais = input("?\n")
            
            if ais == "?":
                try:
                    print("?")
                    time.sleep(1)
                    print("leave, now      ?????")
                    time.sleep(1)
                    try:
                        ai = input("?\n")
                        
                        if ai is input():
                            quit()
                            
                        elif ai is not input():
                            try:
                                ai = False
                                ais =  True
                                if ai is False:
                                    quit()
                            finally:
                                main()
                                
                        elif ai == "???":
                            nu = any
                            print(nu)
                            slice(main)
                            time.sleep(1)
                            try:
                                print(nu)
                                nu1 = random.randint(1,9)
                                nu2 = random.randint(1,9)
                                
                                if nu1 < nu2:
                                    print(nu2, "is more than nu1")
                                    time.sleep(1)
                                    main()
                                    
                                elif nu1 > nu2:
                                    print(nu1, "is more than nu2")
                                    time.sleep(1)
                            finally:
                                main()
                                
                        elif ai == "?":
                            pow(main)
                            slice(main())
                            time.sleep(1)
                            try:
                                num1 = random.randint(1,9)
                                num2 = random.randint(1,9)
                                
                                if num1 is max:
                                    print(num1, "is max")
                                    main()
                                    
                                elif num2 is max:
                                    print(num2, "is max")
                                    main()
                            finally:
                                main()
                        
                    finally:
                        main()
                finally:
                    main()
            else:
                time.sleep(0.5)
        finally:
            main()
            
    else:
        time.sleep(0.5)
        main()
        
main()