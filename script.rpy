define player = Character("[player]", color="#da0b0b")
define robin = Character("Robin", color="#da0b0b")
define raven = Character("Raven", color="#9c119a")
define starfire = Character("Starfire", color="#ff6800")
define beastboy = Character("Beast Boy", color="#0f9c1e")
define cyborg = Character("Cyborg", color="#3bbce3")
define gamedev = Character("GameDev", color="#000000")

default ravenrelationship = 0
default robinrelationship = 0
default cyborgrelationship = 0
default starfirerelationship = 0
default beastboyrelationship = 0

default switch1 = False
default switch2 = False
default switch3 = False
default switch4 = False
default switch5 = False
default switch6 = False
default switch7 = False
default switch8 = False
default switch9 = False
default switch10 = False

label start:
    scene outsidetower
    "You are the newest member of the Teen Titans! Well... probationary member anyways"
    "This all started when you were walking down the street, minding your own business, and saw a young girl walk into traffic."
    "Without even thinking, you stepped between her and an incoming car, holding her close in an attempt to shield her."
    "There was a loud crash, and for a moment you thought the car had managed to swerve out of the way in time, however..."
    "When you turned around, you saw that the car had indeed struck you... but instead of turning you into pavement pizza"
    "the car was completely totaled... hitting your body as if it were a solid steel beam."
    "The ambulance soon arrived to see to the unfortunate driver, and upon inspecting you the paramedics found not a single scratch..."
    "You had never had powers before, and upon drawing blood for tests the needle pierced your skin without issue."
    "You've never shown and superhuman traits before now, and aren't exactly sure what it was that made you impervious to incoming cars... but you are determined to find out."
    "Luckily, upon hearing of your newfound powers, the Titans have offered to take you in, hoping to discover what it was exactly that allowed you to save that little girl,
    and if possible, how to bring those powers under your control"
    jump scene2

label scene2:
    scene insidetower
    show robindefault
    "After what was admittedly a rather nerve wracking car drive sitting next to THE Robin, you find yourself inside THE Titans Tower."
    robin "Well, this is going to be your new home, for the time being. Until we figure out how your powers work and how you can control them, it is safer for everyone if you are kept somewhere you can be monitored."
    "You aren't really sure what to say, you were in shock the whole car ride you remained mostly silent, unable to believe this is actually happening."
    $ player = renpy.input("Which reminds me, what is your name?")
    $ player = player.strip()
    robin "Well, if you have any questions [player], feel free to let me know."
    menu:
        "Where is my room?":
            jump scene3a
        "Nah, I think I'm just going to look around a bit.":
            jump scene3b

label scene3a:
    scene whiteroom
    show robindefault
    robin "Oh yeah, we have a spare room set aside. It's pretty bland, but you can always add a few personal touches later."
    player "Wow... you weren't kidding."
    robin "Yeah, like I said, pretty bland. All our rooms started out this way though, I think it's important for morale to have a place that's yours, especially when living in close proximity to others like we do."
    robin "Anyways, feel free to look around a bit, introduce yourself. I told everyone to expect a new arrival, so they'll be expecting you."
    jump scene4

label scene3b:
    scene insidetower
    show robindefault
    robin "Alright, I notified everyone that you were coming, so they should be expecting you."
    jump scene4

label scene4:
    scene insidetower
    menu:
        "TV area (Beast Boy)" if not switch1:
            jump beastboyintro
        "Garage (Cyborg)" if not switch2:
            jump cyborgintro
        "Roof (Raven)" if not switch3:
            jump ravenintro
        "Obstacle course (Starfire)" if not switch4:
            jump starfireintro
        "Robins room (Robin)" if not switch5:
            jump robinintro
        "Go to bed for the night":
            jump sleep1

label ravenintro:
    scene towerroof
    "After making your way to the elevator you hit the button for the top floor, above the operations center."
    "This room mainly served as storage, and gave access to lighting and security cameras for the ceiling of the floor below."
    "From there it was a short walk up the stairwell to the roof. At this point it was getting fairly late, the sun not quite setting, but low in the sky."
    "The roof had a spectacular view of the city, as well as what looked to be a large court meant for different sports and activities."
    show ravendefault
    "Off to one side there looked to be a meditation area, in the middle of which sat... or rather, levitated, Raven."
    "Raven was of course a famous member of the Teen Titans, you recognize her instantly from various news sources and websites."
    "For a moment you are a little star struck, you'd barely been able to speak to Robin, and he was a fairly... well, welcoming individual in comparison to the famously moody Titan."
    "Apparently you considered how to proceed for a bit too long, as Raven was the first to break the silence."
    raven "Do you intend to just stand there staring, or do you require something?"
    "Although her words sounded like a helpful request, the slight annoyance in her voice indicated otherwise."
    player "Oh, sorry I was just..."
    menu:
        "admiring the view.":
            jump ravenintro2a
        "looking around, Robin told me I should introduce myself to the rest of the team...":
            jump ravenintro2b

label ravenintro2a:
    scene towerroof
    show ravendefault
    "Raven lets out a sigh, feet touching the ground as she turns to face you, a slightly annoyed furrow to her brow."
    raven "What is that supposed to be, some sort of pickup line?"
    menu:
        "Maybe...":
            jump ravenintro2a1
        "I was talking about the city.":
            jump ravenintro2a2

label ravenintro2a1:
    scene towerroof
    show ravendefault
    "You see a twinge of annoyance cross Raven's face, it is only momentary, but unmistakable."
    raven "Not interested"
    "Raven then returns to her meditation, ignoring you completely."
    "You decide it would probably be best to go elsewhere..."
    $ ravenrelationship = ravenrelationship -1
    $ switch3 = True
    jump scene4

label ravenintro2a2:
    scene towerroof
    show ravendefault
    "Raven pauses for a moment, her expression going neutral before blinking."
    raven "Oh, yes... it can be quite... nice, I suppose."
    "After being slightly thrown off by your statement she takes a few steps closer, looking you up and down, but keeping a respectable distance."
    raven "So, Robin says you show some signs of potential... although he wasn't exactly clear as to how."
    player "Yeah, I'm not really sure how it works myself, or if it was even just a one time thing... but he said it would probably be best for me to stay here with you guys until we figure that out."
    "Raven nods, apparently agreeing with that statement."
    raven "If anyone will be able to help you, it's us... until we figure things out, we'll make sure no harm comes to you."
    "You offer Raven a slight smile."
    player "Thanks, that means a lot."
    "Raven doesn't say anything, although you swear you saw her expression shift slightly... maybe a small smile?"
    "Before you can really get a good look she turns her back to you, returning to her meditation."
    $ ravenrelationship = ravenrelationship +1
    $ switch3 = True
    jump scene4

label ravenintro2b:
    scene towerroof
    show ravendefault
    "Raven descends gracefully to the floor, turning to face you. She gives you an appraising gaze, looking you up and down."
    raven "So, Robin says you show some signs of potential... although he wasn't exactly clear as to how."
    player "Yeah, I'm not really sure how it works myself, or if it was even just a one time thing... but he said it would probably be best for me to stay here with you guys until we figure that out."
    "Raven nods, apparently agreeing with that statement."
    raven "If anyone will be able to help you, it's us... until we figure things out, we'll make sure no harm comes to you."
    "You offer Raven a slight smile."
    player "Thanks, that means a lot."
    "Raven doesn't say anything, although you swear you saw her expression shift slightly... maybe a small smile?"
    "Before you can really get a good look she turns her back to you, returning to her meditation."
    $ ravenrelationship = ravenrelationship +1
    $ switch3 = True
    jump scene4



label beastboyintro:
    scene towertv
    show beastboydefault
    "As Robin left the room, your attention is drawn to the far side of the room, towards the large TV screen currently obscuring the view of the city through the large windows."
    "As you approach you can see that Beast Boy, the shape shifting Titan, is slouched over on the couch, a controller in his hands."
    "He appears to be playing a fighting game, fingers mashing away with lightning speed. He is so engrossed in the game that he doesn't really notice your approach."
    beastboy "Almost... almost... DAMMIT!"
    "Beast Boy sighs in defeat as he puts down the controller, a sudden look of surprise on his face as he noticed you're standing there."
    beastboy "Holy sh-... shoot... I uhhh, didn't see you there."
    beastboy "Hey, so you must be the new guy eh? How's it going?"
    player "Alright I guess, just getting a feel for the place."
    beastboy "Cool. Well, I'm Beast Boy... although you probably already knew that."
    "Beast Boy smiles awkwardly, apparently as uncomfortable meeting new people as you are."
    "He smiles suddenly however, a thought occurring to him."
    beastboy "Hey, wanna play a round? The game's two player."
    menu:
        "Nah, I think I'm going to take a look around.":
            jump beastboyintro2a
        "Sure, sounds like fun.":
            jump beastboyintro2b

label beastboyintro2a:
    "Beastboy seems a bit disappointed, but doesn't say anything about it."
    beastboy "Alright, maybe later."
    "With that he returns his attention back to the screen."
    $ beastboyrelationship = beastboyrelationship -1
    $ switch1 = True
    jump scene4

label beastboyintro2b:
    "Beast Boy grins, handing you a nearby controlled."
    "Once you are seated he wastes no time setting up the match. You're familiar with the fighting game, and confident you can hold your own."
    beastboy "Alright, well, don't expect me to take it easy on you just cuz you're the new guy."
    "The match is an intense one, Beast Boy clearly has a lot of experience and skill when it comes to video games."
    "As the match starts to near it's end, you are confident you are going to win... however..."
    menu:
        "Let Beast Boy win.":
            jump beastboyintro3a

        "Destroy him!":
            jump beastboyintro3b

label beastboyintro3a:
    "You decide to slow down a bit near the end, giving Beast Boy the perfect opening to land the killing blow."
    beastboy "Booyeah! You just got owned!"
    "Beast Boy clearly doesn't mind boasting, even doing a little victory dance."
    "However, he soon calms himself down, still grinning ear to ear."
    beastboy "That was a good match, we should definitely play again some time."
    "And with that, you decide it's best to continue exploring the tower."
    $ beastboyrelationship = beastboyrelationship +1
    $ switch1 = True
    jump scene4

label beastboyintro3b:
    "You decide that taking it easy on Beast Boy wouldn't be very sportsmanlike of you, so you go all out, determined to win."
    "You manage to land the finishing blow, the game declaring you the victor."
    beastboy "Dammit! I was this close! THIS CLOSE!"
    "Beast Boy holds his fingers up a fraction of an inch apart, showing how close he was to victory."
    beastboy "Anyways, that was a good game. Don't get too cocky though, I will have my revenge..."
    "Beast Boy shakes your hand, clearly a good sport about losing."
    "With the game finished, you decide it would be best if you continued to explore the tower."
    $ beastboyrelationship = beastboyrelationship +1
    $ switch1 = True
    jump scene4

label cyborgintro:
    scene garage
    "After a quick trip down the elevator, you find yourself on the ground floor. Making your way over to the garage."
    "Inside, you can see Cyborg leaning over the engine of a car, the hood popped."
    show cyborgdefault
    "Cyborg notices you out of the corner of his robotic eye, sitting up."
    cyborg "Hey, you must be the new guy. Can I help you with something?"
    menu:
        "Just taking a look around, what are you up to?":
            jump cyborgintro2a
        "Nothing really, don't mind me.":
            jump cyborgintro2b

label cyborgintro2b:
    cyborg "Alright, well... I'm just going to get back to work then."
    $ cyborgrelationship = cyborgrelationship -1
    $ switch2 = True
    jump scene4

label cyborgintro2a:
    cyborg "Just doing some general maintenance, keeping everything in top shape keeps me from having to do some major repairs down the road."
    "The T-car was an impressive machine, top of the line, with a ton of custom features implemented by Cyborg himself."
    player "Never thought I'd get to see this thing up close... it always looked so awesome on TV."
    "Cyborg grins, clearly rather proud of the T-Car."
    cyborg "Yeah, it's pretty awesome... wanna take it for a spin?"

    menu:
        "Hell yeah I would!":
            jump cyborgintro3a
        "Maybe some other time, not quite settled in yet.":
            jump cyborgintro3b

label cyborgintro3a:
    "Cyborg grins, obviously pumped up by your enthusiasm."
    cyborg "Hop on in then, lets go for a ride."
    "As Cyborg shuts the hood you get into the passengers seat. He then joins you in the car."
    scene townnight
    show cyborgdefault
    "It isn't long till you are cruising down the city streets, people staring as you drive by in the famous car."
    "Along the way you and Cyborg exchange small talk, taking turns flicking through the radio stations."

    menu:
        "Ask to take a turn behind the wheel.":
            jump cyborgintro4a
        "Just enjoy the ride.":
            jump cyborgintro4b

label cyborgintro3b:
    "Cyborg nods understandingly."
    cyborg "Alright, maybe next time."
    "With that, you leave cyborg to his work, making your way back to the control center."
    $ switch2 = True
    jump scene4

label cyborgintro4a:
    show cyborgdefault
    "Cyborg visibly cringes at the question."
    cyborg "Sorry man, no one drives this baby but me. Hope you understand."
    "The rest of the drive is a bit awkward, silent except for the radio. Soon enough, you are pulling into the garage at Titans Tower."
    scene garage
    show cyborgdefault
    cyborg "Well, I've got some work to do, so I guess I'll see you later?"
    "You nod before making your exit."
    $ cyborgrelationship = cyborgrelationship - 1
    $ switch2 = True
    jump scene4

label cyborgintro4b:
    show cyborgdefault
    "You decide it's best not to push, and just enjoy the moment."
    "All too soon, you arrive back at Titans Tower."
    cyborg "That was pretty fun, been a while since I've been out for a drive any it not been an emergency situation."
    player "Yeah, we should do that again some time."
    cyborg "You can count on it. For now though, I should better get back to work."
    "And with that, you leave Cyborg to his repairs, heading back to the control room."
    $ cyborgrelationship = cyborgrelationship + 1
    $ switch2 = True
    jump scene4


label starfireintro:
    "You make your way down to ground level of the Titans Tower before heading out the back door."
    scene trainingground
    "You see in the distance, a purple and orange blur flying through the air, green bolts of energy shooting directly into human shaped targets on the ground with laser like precision."
    "Only after the orange and purple blur came to a stop were you able to make out what exactly it was."
    show starfiredefault
    "Starfire was just as famous as the other Titans, maybe even more so considering her stunning, otherworldly beauty."
    "Upon seeing you, Starfire makes a B line for your location, coming to a sudden stop just a few feet from you."
    starfire "Hello! Are you the new person Robin said was coming? How are you?"
    player "I guess so, and I'm doing well, thank you."
    "Starfire floated around you, looking you up and down with interest."
    starfire "You look normal... perfectly average."
    player "Thanks?... I guess..."
    menu:
        "So, is this where you train?":
            jump starfireintro2a
        "I uhhh, should probably get going.":
            jump starfireintro2b


label starfireintro2a:
    starfire "Yes! Here, and also in the gym. I am only allowed to throw Starbolts outside though, Robin says it's one of the gym rules."
    "You get the feeling that this rule was instated after a rather unfortunate incident occurred in the gym."
    starfire "Follow me, I'll show you."
    "Starfire takes your hand, pulling you along until you stand outside the Titans gym."
    scene gym
    show starfiredefault
    starfire "See, we have weights, treadmills, mats for sparing... oh, we should spar together! On my planet, fighting is a customary way to get to know one another."
    "Before you can really reply, you are being dragged towards the sparring mats. After releasing you, she grabs some gloves and protective head gear, passing you some."
    starfire "Safety is important, once you are ready, we can commence."
    menu:
        "I uhhh, would rather not if that's okay.":
            jump starfireintro3a
        "Put on your gear and get ready.":
            jump starfireintro3b

label starfireintro2b:
    "Starfire looks deflated when you say you need to go."
    starfire "Alright... maybe we can speak again in the future..."
    $ starfirerelationship = starfirerelationship -1
    $ switch4 = True
    jump scene4

label starfireintro3a:
    "You see Starfire deflate before your very eyes."
    starfire "You do not wish to spar? Why?"
    menu:
        "I don't want to hurt you... you're a girl after all.":
            jump starfireintro4a
        "I just don't feel like it...":
            jump starfireintro4b

label starfireintro4a:
    "Starfire looks at you blankly, before bursting into laughter."
    starfire "You won't hurt me. And my race has no rules against hitting women, as we are evenly matched. I am as strong as any man on my planet."
    menu:
        "It just wouldn't feel right...":
            jump starfireintro6a
        "Huh... well, I guess if you say so...":
            jump starfireintro3b

label starfireintro3b:
    "You put on your head gear and boxing gloves. Starfire stands ready, apparently waiting for you to make the first move."
    menu:
        "Hold back, you don't want to hurt her.":
            jump starfireintro5a
        "Give it everything you got.":
            jump starfireintro5b

label starfireintro5a:
    "You decide it's better to take things easy, not wanting to accidentally hurt Starfire."
    "Starfire is light on her feet, and quick too... you manage to dodge a few punches, even block, but it is taking everything in you to keep up."
    "Eventually, Starfire stops without any real explanation, looking sad and annoyed."
    starfire "You are holding back... if you do not wish to spar as equals, than I do not wish to spar with you."
    "Starfire flies off in a huff, clearly offended by your lack of effort."
    "You decide it would probably be best to leave, as there is nothing else to do in the gym."
    $ starfirerelationship = starfirerelationship -1
    $ switch4 = True
    jump scene4

label starfireintro5b:
    "You decide to give it everything you got, sure that the Titan can more than handle anything you can dish out."
    "Starfire is light on her feet, and quick too... you manage to dodge a few punches, even block, but it is taking everything you have to keep up."
    "Eventually, you start to adjust to the rhythm of things, even able to land a few punches, not that Starfire seems to notice. Meanwhile, every punch you block makes your bones rattle."
    "After a few minutes you start to slow down, and Starfire decides that the match is over."
    starfire "You did very well! What matters most is that you did not give up, you gave it everything you had."
    "Starfire is smiling ear to ear, clearly very pleased with the exercise, and seemingly unaffected... meanwhile you are panting, sure you'll have bruises tomorrow."
    player "Yeah, it was fun... although I think I need a bit of a break..."
    "Starfire nods appreciatively."
    starfire "You go rest, I have a few exercises to do. May we spar again soon!"
    "With that, starfire flies off, leaving you to limp away, back to the control center."
    $ starfirerelationship = starfirerelationship + 1
    $ switch4 = True
    jump scene4

label robinintro:
    "You decide after taking a quick look around to see what Robin is up to, walking by his room, the door to which is open."
    scene robinsroom
    show robindefault
    "Robins room is a rather... gloomy looking place, with pictures of criminals and news clippings on the wall, some attached with string like in those crime TV shows."
    "One side of his room consists of a work bench, no doubt where he puts together some of his gadgets. A computer sits on a desk in the far corner."
    player "Mind if I come in?"
    robin "Sure, what can I help you with?"
    jump robinquestions

label robinquestions:
    menu:
        "I was wondering, is there anywhere in the tower I should avoid?" if not switch6:
            jump robinintro1a
        "So, when do I get a superhero name?" if not switch7:
            jump robinintro1b
        "I just wanted to say thanks, for helping me out with this power stuff." if not switch8:
            jump robinintro1c
        "Nah, just looking around.":
            "You decide to head back to the operations center."
            $ switch5 = True
            jump scene4

label robinintro1a:
    "Robin considers your question carefully."
    robin "Well, for the most part the tower is completely open to you. Cyborg entered your face into the security systems white list, so you get just as much access as anyone else."
    robin "That said, there are some limits. The security room requires facial recognition and a communicator to get inside, and you don't have one of those."
    robin "There's also some common sense ones... you won't be able to just walk into someones room without their permission, unless they've left the door unlocked."
    robin "Even if they did, it would be better for you not to go inside without permission... especially Raven's room, trust me... don't sneak into Raven's room."
    "There is obviously a story there, but you don't push the matter and further."
    $ switch6 = True
    jump robinquestions

label robinintro1b:
    "Robin looks at you, a bit confused by the question."
    robin "Well, you aren't exactly a superhero just yet... lets focus on getting your powers under control before we get to picking out names and costumes."
    robin "Besides, this isn't a game... it isn't about dressing up and cool catch phrases. We deal with life and death situations, this isn't like the comics, kid."
    $ robinrelationship = robinrelationship -1
    $ switch7 = True
    jump robinquestions

label robinintro1c:
    "You see a small smile appear on Robin's face, it is only there for an instant, but you manage to notice it before it vanishes back to his normal, serious expression."
    robin "You're welcome, but you should know, we are doing this just as much for the city's safety as we are for your own."
    robin "Uncontrolled powers can cause some serious accidents... you were lucky, you saved a life, but you could have just as easily ended up crushing the girl, and killing the driver."
    "Robins tone sounds even more serious than usual."
    robin "It is my hope that we can help you to control your powers... but make no mistake, we see you as a potential threat, and it is our job to make sure you can be controlled."
    $ robinrelationship = robinrelationship +1
    $ switch8 = True
    jump robinquestions

label sleep1:
    "You decide you've had a pretty long day, and head to your plain white room to get some rest."
    "Once in bed, it takes you a while to actually fall asleep... after the excitement of today, who could blame you? And who knows what tomorrow will bring..."
    "Raven:  [ravenrelationship] Cyborg:  [cyborgrelationship] Beast Boy:  [beastboyrelationship] Starfire:  [starfirerelationship] Robin:  [robinrelationship]"
    $ switch1 = False
    $ switch2 = False
    $ switch3 = False
    $ switch4 = False
    $ switch5 = False
    $ switch6 = False
    $ switch7 = False
    $ switch8 = False
    jump day2

label day2:
    scene whiteroom
    "The next morning, you awaken to the sound of an alarm. It doesn't sound like an emegency, more like the kind of alarm you'd set to wake up in the morning."
    "After a few moments, you groan as you sit up, feeling like you could use another few hours after the excitement of yesterday."
    "After the alarm stops, you hear Robins voice over the loud speaker."
    robin "Good morning Titans, please report to the command center, that includes you [player]."
    "You groan, dragging yourself out of bed, getting dressed before heading out into the command center, where the other Titans were waiting."
    scene insidetower
    show robindefault
    "As you enter the room, everyone there looks to be wide awake and ready to face the day... except Beast Boy, who looks just as tired as you, rubbing his eyes and yawning."
    robin "Well [player], today is going to be your first real day of training... we've got to figure out how exactly your powers work, and if it is possible to control them."
    robin "With this in mind, you are going to take turns training with each of us. We all have our own ideas on how best to bring out your abilities... so it seemed like a good idea to test them all independantly."
    "You listen, nodding along as Robin explains his reasoning."
    robin "So, while you train, the rest of us will be seeing to our usual duties, tagging in the next person you choose to train with after about... two hours or so."
    "You look at robin, mouth agap... two hours times five Titans is ten hours of solid training."
    robin "What? No one said this was going to be easy. You'll get a lunch break, and the team knows to be careful not to break you."
    "You see Cyborg grinning out of the corner of your eye, but when you turn to look he's back to acting professional."
    robin "So, you can grab a quick breakfast, but then I expect you to tag one of us in so we can get started."
    "You shuffle off to the kitchen area, as if in denial about the torment that awaits you... ten hours of training with super powered heros... this was not going to be easy."
    "You eat breakfast in a bit of a daze, operating on autopilot as you chew a breakfast bar and drink a cup of orange juice, which you try to make last as long as reasonably possible."
    "All too soon however, the time comes for you to make a choice... who is going to train you first?"
    jump teamchoice

label teamchoice
    menu:
        "Raven":
            jump raventraining
        "Starfire":
            jump starfiretraining
        "Beast Boy":
            jump beastboytraining
        "Cyborg":
            jump cyborgtraining
        "Robin":
            jump robintraining

label raventraining:
    "You make your way over to Raven, who seems to be scrolling through some police reports with Robin on a tablet. Both look at you as you approach."
    player "Hey Raven, is now a good time to get started?"
    "Raven doesn't respond verbally, simple floating off, expecting you to follow her."
    scene towerroof
    show ravendefault
    raven "I looked over Robin's report on your incident... he says you claim to never have experienced something like this before, is that correct?"
    "You nod in confirmation."
    player "Nope, pretty sure I'd remember being able to stop a racing car."
    "Raven roles her eyes."
    raven "It may not be that obvious... did you ever experience anything strange? Something you couldn't explain?"
    "You think back, combing through memories of your early childhood. Nothing particularly special comes to mind."
    player "Nah... I've always been pretty normal."
    "Raven sighs, apparently not finding your input very helpful."
    raven "Well, if we have nothing to go on, we should start by focusing on the earliest incident we know of, the car crash."
    "Raven guides you over to a set of meditations pads on the roof, reminding you of the sort of pads they brough out in gym class to keep anyone from getting injured from a fall."
    raven "I want you to take a seat and relax... take a few deep breaths... and focus on your center."
    "Although not entirely sure what your \"Center\" was supposed to be, you sit down and take a few deep breaths, trying to relax and focus."
    raven "Now, I want you to think back to that moment, when you saw the car heading towards the little girl... picture it in your mind, replay it, relive it as if it is happening now."
    "You do as Raven instructs, taking a few more deep breaths as you picture that moment... it was honestly a bit of a blur, you just acted on instinct, and it was over before you could really process what was happening."
    player "It's not working... I don't feel any different..."
    "You can practically feel Raven rolling her eyes at you, can hear it in her tone of voice."
    raven "Of course not, you thought that you'd have a breakthrough in the first five minutes? Meditation takes time, patience... now, clear your mind, and focus on that moment."
    "As the minutes tick by, you find it harder and harder to keep focus, Raven snapping her fingers every now and then when you start to fidget or your mind starts to wander, although how she knows that is beyond you."
    "Slowly, it starts to get a bit easier to keep your mind on the task at hand. The image in your mind becomes a little clearer... feels just that little bit realer..."
    raven "That's it!"
    "Raven's voice breaks you out of the deep trance you were in, causing you to take a sharp breath as your eyes open."
    player "That's what? I didn't feel anything."
    "Raven shakes her head."
    raven "Of course you didn't... but I did. I felt a flicker of energy around you, just for a moment..."
    "Raven takes a closer look at you, placing her hands on your shoulders before closing her eyes."
    "You feel a cool energy surround you, like a breeze on a hot day. You can feel it slide up your arms, around your shoulders, searching, going deeper."
    "You feel a bit... violated, tensing up on reflex."
    raven "Relax... don't fight me. This is hard enough as it is without your resistance."
    "Her tone is a bit annoyed, but you get the sense that it isn't at you... more of a sound of focus and frustration with the problem than with you personally."
    "You take another deep breath, trying to keep from squirming as that strange energy slides deeper inside of you, like tendrils of cold air inside your body..."
    "You don't have much to look at besides Raven, who's brow is currently furrowed in concentration, head slightly bowed, drawning in slow breaths through her nose and letting them out through her mouth."
    "When her eyes open suddently you find yourself staring directly into her gaze, her face only a few inches from yours."
    raven "Whatever it is, it's gone."
    "She draws away, turning back to look out over the city."
    raven "I don't know if it's magic, or something... else... but it was definitely there, and you seem to have some control over it... deep down."
    player "Should I try meditating some more?"
    "Raven shakes her head."
    raven "We only have about fifteen minutes left in our session. I doubt you will be able to get into that deep a meditation in that time on your second try."
    menu:
        "So... can I go?":
            jump raventraining2a
        "You said it could be magic... how does magic work exactly?" if not switch1:
            jump raventraining2b
        "So, do you think I can learn to control it." if not switch2:
            jump raventraining2c

label raventraining2a:
    "Raven shrugs indifferently."
    raven "Do what you like, I consider our session over."
    "With that you decide it to take a few minutes to relax, before heading back to the command center."
    jump teamchoice

label raventraining2b:
    "Raven pauses, considering how to answer that question for a moment."
    raven "That's sort of like asking how technology works... there are many subsets of magic, some would say an infinite number."
    raven ""

return
