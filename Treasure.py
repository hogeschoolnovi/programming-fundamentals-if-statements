# Je gaat een nieuw programma schrijven, genaamd Treasure.py. Dit programma is een spel waarbij de speler een aantal keuzes moet maken.
# Je mag zelf bepalen wat de keuzes zijn en wat de uitkomsten zijn van de keuzes. Het spel moet minimaal 4 verschillende keuzes bevatten.
# Het einde van het spel is een if elif else statement.
#
# Voorbeeld:
# Welkom op het eiland van de schat.
# Je bent op een kruispunt, ga je links of rechts?
# Rechts
#  Helaas heb je verkeerd gekozen en ben je in een gat gevallen. Game Over.
#
# Of:
# Welkom op het eiland van de schat.
# Je bent op een kruispunt, ga je links of rechts?
# Links
# Je komt bij een meer, ga je zwemmen of wachten?
# etc...

print("""
                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. \\
    .-' ..::--""_(##)#)"':. \\ \\)    \\ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\\.-'
   "  / |  :' :/""\\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\\.___./'-.
    / :/|\\ :\\_:\\   \\#//\\            /  |  \\
    |:/ | ""--':\\   (#//)              '
    \\/  \\ :|  \\ :\\  (#//)
         \\:\\   '.':. \\#//\\
          ':|    "--'(#///)
                     (#///)
                     (#///)         ___/""\\     
                      \\#///\\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.\\
                      (##///)        ||o   \\\\
                       \\##///\\        \\-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::''':::     "" - -.._
                  __..-'''           __;: :            "-._
          __..--""                  `---/ ;                '\\._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     ""--...  ___""'''-----......._______......----""'     --""
                          ---.....   ___....----             
""")


# Schrijf hier je code:

print("Welkom op het eiland van de schat.")
print("Je bent op een T-splitsing, ga je links of rechts?")
left_right = input("Links of Rechts? ")
if left_right == "rechts":
    print("Helaas heb je verkeerd gekozen en ben je in een gat gevallen. Game Over.")
else:
    print("Je komt bij een meer, ga je zwemmen of wachten?")
    swim_wait = input("Zwemmen of Wachten? ")
    if swim_wait == "zwemmen":
        print("Je hebt gezwommen, helaas vond een forel je tenen lekker en heeft je voet opgegeten. Game Over.")
    else:
        print("Je hebt niet gezwommen, na een uur wachten kwam er een boot,"
              " je bent op een eiland gekomen ga je links over het zandpad of rechts door de grot?")
        left_right = input("Links of Rechts? ")
        if left_right == "rechts":
            print("Je bent de grot in gegaan, hier kwam je 3 deuren tegen, Rood, Geel, Blauw.")

            door = input("Welke deur wil je openen, Rood, Geel, Blauw? ")
            if door == "rood":
                print("Achter de deur was een vlam, je bent verbrand. Game Over.")
            elif door == "geel":
                print("Achter de deur was de schat, je hebt gewonnen!")
            elif door == "blauw":
                print("Achter de deur was een beest, het heeft je vermoord. Game Over.")
            else:
                print("Je hebt geen deur geopend, je hebt niet gezwommen,"
                      "je bent niet naar rechts gegaan, wat doe je eigenlijk? Game Over.")
        else:
            print(
                "Je bent links gegaan, je bent in een moeras beland. En hebt daar een vliegje ingeslikt... Game Over.")
