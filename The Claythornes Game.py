import os
from textwrap import dedent
from sys import exit

############################################################Global variables 
extra_info_of_edward = []
stuff_we_know_about_edward = {"Name:": "Edward Claythorne", "Relationship:": "Victim", "Extra information:": extra_info_of_edward}
your_files = {"Edward Claythorne": stuff_we_know_about_edward}


attempts = 0
############################################################First event

############################################################Characters' information in dictionary format 
servant_dict = {"name" : "Servant (Lupe Perez)",
"cause_of_death" : None,
"relationship" : None,
"position" : "Servant",
"testimony" : "Edward and Elsa were talking in the dining room.. They asked me to make some tea.. I prepared the tea but as soon as I had poured the tea on the teacups, Mr Lombard called me demanding me to look for some aspirins as he was having a headache.. I asked him to let me give Edward and Elsa their tea, but he insisted that it was urgent.. So, I left the kitchen to fetch the aspirins.. I didn't find any aspirins in the room where we normally store them, so it took me longer than it would normally have.. During that time anyone could have entered the kitchen and poisoned Mr Claythorne's tea.. When I found the aspirins, I took them upstairs to Mr Lombard.. He was reading some papers, they look like official papers.. He seemed quite stressed.. When I asked him if he needed anything more, he offered me some money in exchange of any information I had about Edward and Elsa.. I told him the little I knew, and that Edward was having an affair with my daughter.. I told him that Edward had fired my daughter and me and that had offered me a handsome amount of money to leave immediately.. We were to leave next day.. When I returned to the kitchen, I noticed that someone had been looking for something on the cupboard as the cupboards were now a bit messy and one door was left open.. At the time, I didn't find it odd, so I just took the tea to Edward and Elsa.. I would normally have had reheated the teas, but since Mr Edward and I were not exactly on good terms anymore, I didn't care.. He had technically fired me and that was my last day of service there.. When I enter the room to leave the teas, I noticed that only Elsa was there.. Mr Edward seemed to have left room to answer an urgent business call.. He was in a different room, if Elsa wanted to poison the tea, she had the chance to do it.. After that, I returned to the kitchen and clean up the little mess.. I was in the kitchen when Edward died.. I called the ambulance.", 
"evidence" : None, 
"accusing_dialogue" : "You killed your master.. You hated him because he had had an affair with your only daughter, an 18-year-old.. He offered you some money to keep quiet, but it wasn't enough, after all, you had also been fired and you were to leave next day.... unless.... you killed him!", 
"alibi" : "I hated him alright, but I would have never kill him.. I always knew what kind of man he was.. But I thought that my daughter was smarter than that.. I was angry at me for not raising her properly.. I was already looking for another job.. Mrs Lombard was going to help me find a new job among her connections.. So, I was not worried about that.. I can't believe you think me capable of murdering someone for something as petty as that.",
"extra_info" : None,
"what_they_knew_about_edward": ["He was having tea with Elsa when he died."]}

william_dict = {"name" :"William Claythorne", 
"cause_of_death" : None,
"relationship" :"Edward's brother", 
"position" :"Head of IT department at Foogled Corp", 
"testimony" :"(says nervously) I was in the golf course when I received the news.. I was quite shocked by the news of my brother's death.. I don't know anything else.", 
"evidence": None,
"accusing_dialogue" :"William Claythorne, you murdered your eldest brother.. You have always been in love with his wife.. You couldn't get over her even after they got married.. You remained always there hoping that one day she would be yours.. You always fought with your brother when he hurt Catherine with his affairs.. But he simply didn't care.. With time, she learned to cope with it, and the relationship between your brother and you improved.. However, this time it was different, he was going to leave Catherine and she almost committed suicide because of it.. You proposed to her, but she told you that while Edward was alive she would love him.. So, you took the matter into your own hands.. After leaving her room, you went downstairs and poisoned the tea.", 
"alibi" :" I find it quite insulting that you think me capable of murdering my brother! Sure, we had our differences and I have always loved Catherine.. I was in range when I realized how much he had hurt her, I was going to talk to him at night to talk to sense to him but nothing more.. I hoped that once Catherine knew that I loved her enough to convince my brother not to leave her, that she would fall in love with me and we would finally marry.. I assure you that I didn't kill my brother.",
"extra_info" : None,
"what_they_knew_about_edward": None}

edward_dict = {"name" :"Edward Claythorne", 
"cause_of_death" : "Coniine poisoning.",
"relationship" :"Murder victim.", 
"position" : None,
"testimony" : None,
"evidence" : "Poison bottle and tea cup.", 
"accusing_dialogue" :"Edward killed himself.. He poured the poison to his own tea.", 
"alibi" :"You gotta be kidding me! I'm sure it was murder, a guy like Edward would never kill himself.", 
"extra_info" : [],
"what_they_knew_about_edward": None}

catherine_dict = {"name" :"Catherine Claythorne", 
"cause_of_death" : None,
"relationship" :"Edward's wife", 
"position" : None,
"testimony" : "I wasn't feeling well and decided to go to my room and as I was getting upstairs, I saw Lawrence leave the house.. I think he didn't see me, he seemed anxious and quite angry, but I'm not sure why.. Anyway, I stayed in my room till I heard the news about my husband's death.. I couldn't believe it.. It must have been Elsa.. My husband was not perfect, he was always having affairs.. I had gotten used to it, but Elsa hadn't.. My husband had an affair with an 18-year-old girl and I think that it was too much for Elsa to take in, I heard them fight earlier in the morning.. Edward promised not to see the girl again and to fire the girl and his mother, as both were working for us at the house.. They were given notice and they were to leave the very next day.. But I supposed that wasn't enough for Elsa..", 
"evidence" : None,
"accusing_dialogue" : "Catherine Claythorne, you murdered your husband.. You bought the poison to kill yourself but after talking to William you realized that the one that deserved to die was Edward, not you.. After William left your room, you went downstairs to poison the tea.. If Edward couldn't be yours, he should just die.. And if you were fast, you'll keep the house, the cars and the money.", 
"alibi" : "I find it quite insulting that you think me capable of murdering my husband.. I loved him so much, I can't live without him! I would never kill him!",
"extra_info" : None,
"what_they_knew_about_edward": ["He had slept with his servant's 18-year-old daughter and he tried to buy his way out of it."]}

elsa_dict = {"name" :"Elsa Marston", 
"cause_of_death" : None,
"relationship" :"Edward's fiancée", 
"position" : None,
"testimony" :"Edward was going to divorce Catherine to marry me.. I know she didn't take well the news because an hour before Edward died, William went to talk to Edward, I didn't hear much.. All I know is that he said that Catherine had bought poison to kill herself.. Honestly, I couldn't care less what she did to herself.. If she was that stupid to die because someone didn't want to be with her anymore, well that was her call.. I thought that it was natural selection at its finest.. Of course, after that, I didn't imagine she would use the poison to kill Edward instead! Edward had changed his will, he was leaving Catherine with nothing and everything to me.. I find it quite convenient that she killed him the day before the will was going to go into effect.. She couldn't accept that she was losing her husband and her lifestyle! She even sent her mommy to try to bribe me to leave Edward! As if I was going to accept such a thing! I remember Emily saying before leaving the room 'You'll regret it! I'll make sure you get nothing!' I hope those two rot in prison.", 
"evidence" : None,
"accusing_dialogue" :"Elsa Claythorne, you murdered your fiancé.. You couldn't stand him cheating on you.. As soon as he left the room, you poisoned his tea..", 
"alibi" :"Why would I kill him the day before the will went into effect? That's nuts! I'm innocent and now I'm also broke!",
"extra_info" : None,
"what_they_knew_about_edward": ["He was going to divorce Catherine to marry Elsa.", "He had changed his will and it was going to go into effect the next day, leaving Catherine with nothing.", "Catherine claims to have bought the poison to commit suicide and to have drop it by accident somewhere around the house after William talk him out of it"]}

bree_dict = {"name" : "Bree Claythorne", 
"cause_of_death" : None,
"relationship" : "Edwards's 11-year-old daughter", 
"position" : None,
"testimony" : "I was exploring as usual.. I started in the garden but then I decided to go and see the ducks that were in the lake next to the golf course.. I saw mom and William talking.. Mom seemed sad, she was crying.. I saw them walk towards the house and I went to see the ducks.. After a while, I decided to go to the kitchen to get some bread to feed them.. So, I went.. I was feeding the ducks when I heard about dad's death.", 
"evidence" : None,
"accusing_dialogue" : "Bree Claythorne, you killed your father.. You saw your mother and William talking after she tried to use the poison to commit suicide.. After he talked her out of it, they walked towards the house and accidentally dropped the bottle with the poison to the floor.. You must have found it on your way home.. Since you overheard part of the conversation, you knew what it was.. Once in the kitchen you decided to pour the content on one of the teas.. Would it kill Elsa? Would it kill your father? It didn't matter to you, both of them had made your mother suffer and you hate them for that.", 
"alibi" : "I was hoping it was Elsa, I think she deserved it more! I think mommy will be happier without daddy! He was always making her cry! You are an excellent detective!",
"extra_info" : None,
"what_they_knew_about_edward": None}

philip_dict = {"name" : "Philip Lombard", 
"cause_of_death" : None,
"relationship" : "Catherine's father, he is visiting his daughter at Edward's house", 
"position": "Retired",
"testimony" : "I had a lot of things to do.. I decided to go to my room to go over some papers that I needed to check.. I saw Bree playing outside in the garden as usual and that's all I know.", 
"evidence" : "The paper he was reading was Edward's new will", 
"accusing_dialogue" : "Philip Lombard, you killed your son-in-law.. After you learned everything he had put your daughter through, you decided to call the maid, distract her with some meaningless task while you entered the kitchen to poison the tea.. You couldn't help it, he was not only divorcing your daughter but also, he was going to leave her penniless and humilliated.. So, the day before the will went into effect you decided to protect her.",
"alibi" : "Sure, I was angry at him for all he had done to my daughter over the years.. However, I didn't need to kill him to protect her from the change in the will.. I spent all morning going over the will and the prenup.. I had sent the files to the best lawyer in the country, Mr Thomas Legge, and we had found a loophole.. Mr Legge sent our case right away to Edward's lawyer.. We were going to win the case.. I wouldn't risk going to prison for something I could achieve in a more civilized matter.. However, I'm thankful to whoever killed that son of bitch!",
"extra_info" : None,
"what_they_knew_about_edward": None}

emily_dict = {"name" : "Emily Lombard", 
"cause_of_death" : None,
"relationship" : "Catherine's mother, she is visiting her daughter at Edward's house",
"position" : None,
"testimony" : """I was tired and wanted to relax with a bath.. As I was walking to my room overheard this conversation between William and Catherine: 

	'Catherine: How can you find me attractive? I'm not 20 anymore, I cannot hold a candle to Elsa's youth.. 
	William: I have always found you beautiful, I love you since we were in college, I cannot stand to see you suffer for my brother.. 
    Leave him and marry me instead..
	Catherine: You are my rock, but I cannot marry you.. 
    As long as Edward lives I will love him even if he is with someone else..
	William: I will not give up, I'll make sure that we end up together.. 
    I love you and I'll always do.'

I heard them approach the door.. I didn't want to appear nosy, so I went downstairs to make sure they didn't see me near the door.. As I saw William leave Catherine's room, I noticed that his hair was a bit messed up as if they had been.... I greeted William and he flushed.. I walked to my room.. I was taking a bath when I heard about my son-in-law's death.""", 
"evidence" : None,
"accusing_dialogue" : "Emily Lombard, you've killed your son-in-law.. You tried to help your daughter by bribing Elsa.. You thought it would be that simple, but it wasn't.. In range, you revealed your plans.. You would kill your son-in-law before the will went into effect to leave Elsa with nothing! 'You fool', you told her.",  
"alibi" : "My husband and his lawyer had been going over the will and the prenup.. They found a loophole which would leave Elsa with nothing! That's what I meant! I'm not that stupid to kill someone! But I'm grateful to whoever killed him!",
"extra_info" : None,
"what_they_knew_about_edward": None}

lawrence_dict = {"name" : "Lawrence Wargrave", 
"cause_of_death" : None,
"relationship" : "Edward's best friend", 
"position" : "Manager of the Marketing Department at MacArthur Corp", 
"testimony" : "I went to Edward's house to drop some written proposals that Edward wanted to review.. It was around 4:30.. The servant led me in and I dropped the files in his office.. As I was getting myself out, I overheard some female voices.. I didn't mean to eavesdrop.. It was Emily Lambard and Elsa Marston.. They were arguing.. It seemed that they were quite worked up and I heard Emily say 'You fool! You'll regret it! I'll make sure you get nothing!'.. I left the house and, in my way home, I received the news of Edward's sudden death..", 
"evidence" : "The proposals Edward requested from him were about a project that Lawrence was directing, Edward wanted to evaluate the project again to see if it was worthy of the company's money.. He was likely to shut down Lawrence project as soon as he became CEO..",
"accusing_dialogue" : "Lawrence Wargrave, you murdered your friend Edward Claythorne.. You have always been jealous of him, and when he received that big promotion, you couldn't stand it anymore.. He was going to become your boss and he was going to cancel your big project.. You saw your opportunity to get rid of Mr Claythorne.. You dropped the files and then on the way out you stopped by the kitchen to poison the tea and left the house.. You thought your plan was perfect and that nobody had seen you, but Catherine saw you anxious as you exit the house.. You cannot even conceal your happiness about his death.. You haven't stopped smiling since you heard about his death.", 
"alibi" : "I find it quite insulting that you think me capable of murdering my best friend! I arrived at the house to leave the papers he had requested.. Of course, I was angry about his promotion, he didn't deserve it more than I did.. I was anxious about my project.. Edward had talked about shutting it down even though he knew how much that project meant to me.. As I was leaving the house, I decided to stop by the office to appeal the decision of Edward's promotion.. Although I won't deny that I'm happy about my promotion, I can assure you sir that I'm completely innocent..",
"extra_info" : "He was jealous when he heard that Edward was named new CEO.. He was appointed CEO after Edward's death.",
"what_they_knew_about_edward": None}


############################################################Functions
def print_after_user_ready(txt):
    txt = txt.split(". ")
    for line in txt:
        print(line)
        waiting = input("(Press C to continue)")
        os.system('cls')

def add_info_to_files(character_name):
        if character_name.name not in your_files:
            your_files[character_name.name] = character_name.information
        if character_name.relationship != None:
            character_name.information.update({"Relationship" : character_name.relationship})
        if character_name.position != None: 
            character_name.information.update({"Position": character_name.position})
        if character_name.testimony != None: 
            character_name.information.update({"Testimony": character_name.testimony})
        if character_name.evidence != None: 
            character_name.information.update({"Evidence": character_name.evidence})  
        if character_name.extra_info != None: 
            character_name.information.update({"Extra_info": character_name.extra_info})
        if character_name.what_they_knew_about_edward != None:
            extra_info_of_edward.append(character_name.what_they_knew_about_edward)

def ensure_lenght_of_reply(user_name):
    while len(user_name) < 1:
        print("Sorry I didn't get your name, can you repeat it, please?")
        user_name = input("You: ")
        os.system('cls')
    return user_name     
    
###########################################################Classes' definitions 
class Character(object):
    def __init__(self, info):
        self.name = info["name"]
        self.cause_of_death = info["cause_of_death"]
        self.relationship = info["relationship"]
        self.position = info["position"]
        self.testimony = info["testimony"]
        self.evidence = info["evidence"]
        self.accusing_dialogue = info["accusing_dialogue"]
        self.alibi = info["alibi"]
        self.extra_info = info["extra_info"]
        self.information = {"Name": self.name}
        self.what_they_knew_about_edward = info["what_they_knew_about_edward"]
        
class Actions(object):
    def solve_mystery(self, character_name):
        global attempts
        attempts += 1
        print_after_user_ready(f"You: I have solved the mystery! It was {character_name.name}.")
        print_after_user_ready(f"You: {character_name.accusing_dialogue}")
        if character_name.name == "Edward Claythorne":
            print_after_user_ready(f"Assistant: {character_name.alibi}")
        else:
            print_after_user_ready(f"{character_name.name}: {character_name.alibi}")
            if character_name.alibi != None:
                character_name.information.update({"Second testimony" : character_name.alibi})
        if character_name.name == "Bree Claythorne":
            print("Congrats!")
            waiting = input("Press E to exit")
            exit("Congrats!")
        
    
    def question_witness(self, character_name):
        print_after_user_ready(f"You: Let's go to visit {character_name.name}!")
        if character_name.name == "Edward Claythorne": 
            print_after_user_ready("Assistant: Unless you can speak with the dead, I don't see how.. Stop playing around!")
        else: 
            print_after_user_ready(f"You: Good afternoon, {character_name.name}.. I'm detective {user_name}.. We're here to ask you some questions regarding the death of Mr Edward Claythorne.. ")
            print_after_user_ready(f"{character_name.name}: Of course! {character_name.testimony}")
            print_after_user_ready(f"You: Thank you so much for your time! Have a nice day!")
            print_after_user_ready(f"{character_name.name}: I'm glad I could be of assistance!")
            add_info_to_files(character_name)
            if character_name.extra_info != None:
                print_after_user_ready(f"Assistant: Detective {user_name}! We have found the following information about {character_name.name}: {character_name.extra_info}")
        
    def look_up_files():
        pass

class Event(object):
    def display_text(self, txt):
        self.txt = txt
        print_after_user_ready(txt)
    
    def display_question(self, txt, answers, aut_replies):
        self.txt = txt
        self.answers = answers
        self.aut_replies = aut_replies
        split_text = txt.split(". ")
        print(txt)
        user_reply = input("You: ")
        os.system('cls')
        while answers[0] not in user_reply:
            if answers[1] not in user_reply:
                print(aut_replies[2])
                user_reply = input("You: ")
                os.system('cls')
            else: 
                if aut_replies[1].endswith("?"):
                    print(aut_replies[1])
                    user_reply = input("You: ")
                    os.system('cls')
        if answers[0] in user_reply:
            print(aut_replies[0])
            waiting = input("(Press C to continue)")
            os.system('cls')
    
    def event_inside_event(self, txt, answers, aut_replies):
        self.txt = txt
        self.answers = answers
        self.aut_replies = aut_replies
        print(txt)
        user_reply = input("You: ").lower()
        os.system('cls')
        while answers[0] not in user_reply and answers[1] not in user_reply:
            print(aut_replies[2])
            user_reply = input("You: ").lower()
            os.system('cls')
        if answers[1] in user_reply:
            print(aut_replies[1])
            waiting = input("(Press C to continue)")
            os.system('cls')
        if answers[0] in user_reply:
            event2 = aut_replies[0]
            print(event2[0])
            user_reply = input("You: ").lower()
            os.system('cls')
            while event2[1] not in user_reply:
                if event2[2] in user_reply:
                   print(event2[4])
                   user_reply = input("You: ").lower()
                   os.system('cls')
                if event2[2] not in user_reply and event2[1] not in user_reply:
                    print(event2[5])
                    user_reply = input("You: ").lower()
                    os.system('cls')
            if event2[1] in user_reply:
                print(event2[3])
                waiting = input("(Press C to continue)")
                os.system('cls')
    
    def ask_user_name(self):
        print("Assistant: Hello detective! I'm here to help you anyway I can! My name is Jane! How should I call you?")
        user_name = input("You: ")
        os.system('cls')
        user_name = ensure_lenght_of_reply(user_name)
        print(f"Detective {user_name}, then. Did I get it right? (yes or no?)")
        user_reply = input("You: ")
        os.system('cls')
        while "yes" not in user_reply:
            if "no" in user_reply:
                print("Oh sorry about that, I must be a bit deaf, can you repeat your name again, please?")
                user_name = input("You: ")
                ensure_lenght_of_reply(user_name)
                os.system('cls')
                print(f"Detective {user_name}, then. Did I get it right? (yes or no?)")
                user_reply = input("You: ")
                os.system('cls')
            if "yes" not in user_reply and "no" not in user_reply:
                print(f"Sorry, I didn't get that! Detective {user_name}, then. Did I get it right? (yes or no?)")
                user_reply = input("You: ")
                os.system('cls')
        print(f"Dectective {user_name}, then. Nice to meet you!")
        waiting = input("(Press C to continue)")
        return user_name
                
############################################################Characters 
servant = Character(servant_dict)
william = Character(william_dict)
edward = Character(edward_dict)
catherine = Character(catherine_dict) 
elsa = Character(elsa_dict)
philip = Character(philip_dict)
bree = Character(bree_dict)
emily = Character(emily_dict)
lawrence = Character(lawrence_dict)
##############################################################Other variables

full_list_of_suspects = ["servant", "william", "edward", "catherine", "elsa", "philip", "bree", "emily", "lawrence"]
#suspects = [servant.name, william.name, edward.name, catherine.name, elsa.name, philip.name, bree.name, emily.name, lawrence.name]
possible_actions = ["Look at my files", "Question witness", "Solve mystery"]
suspects_again = {servant, william, edward, catherine, elsa, philip, bree, emily, lawrence}
##############################################################Beginning
def starting():
    event1 = Event()
    event1.display_text(":::Inspired in Agatha Christie's stories:::")
    event1.display_text("This is the story of Catherine Claythorne.. When she was in college, she was a beauty and her best friend, William Claythorne, an IT genius fell in love with her.. However, she decided to married William's brother, Edward Claythorne.. After college Edward and his best friend, Lawrence Wargrave, started working for MacArthur Corp and they have been climbing the corporate ladder ever since.")            
    event2 = Event()
    event2.display_question("(You received a call from your best friend) Hello Catherine, are you free next weekend? Let's go and grab a coffee and catch up! What do you say? Yes or no?", ["yes", "no"], ["Great! I see you then at Grinders Cafe at 7:00.", "Come on Cath, don't make me beg you, please? Yes?", "Sorry, I didn't catch that! What do you say? Yes or no?"])
    event3 = Event()
    event3.display_text("(Saturday 8:00 am - Your 13-year-old daughter Bree Claythorne enters to you room) Bree: Mommy why are you crying? Is it because of papa again?. You: It's nothing, I think I'm just tired.. Bree: I know it's my father's fault and that E-l-s-a! I HATE her!. You: No, darling, Elsa and your father are only friends! Don't think about it! I'm fine.")
    event4 = Event()
    event4.display_text("(Saturday 7:00 pm - Grinders Cafe) Your friend: Hello Catherine, why do you look so down?. You: Edward is having another affair.. Your friend: That bastard! Ever since you married him it's been one affair after another!. You: I know but I love him so much!. Your friend: Don't be a fool! Divorce him and take half of what he owns!. You: I can't! I love him!")
    event5 = Event()
    event5.display_text("(Saturday 11:00 pm - House - William arrives) William: Catherine? What happened?. You: It's Edward, he is leaving me for Elsa!. William: I'll talk to him!! Don't worry everything will be alright!")
    event6 = Event()
    event6.event_inside_event("(Sunday 11:00 am - House - You hear a noise downstairs.... maybe.... it's Edward. What do you want to do? Run downstairs or mind your own business?)", ["downstairs", "mind"], [["(Sunday 11:00 am - Living room - Edward is on the floor with his nose bleeding - William is in range - Elsa is screaming.. What do you want to do? Help Edward or leave the room?", "help", "leave", "Edward doesn't want your help!", "Are you sure? Maybe you should help, he is your husband after all! Write 'help' to say yes.", "Sorry, I didn't catch that, what do you want  to do? Help Edward or leave the room?"] ,"Ok, let's go and take a bath then.","Sorry, I didn't catch that! Do you want to go downstairs or mind your own business?"])
    event7 = Event()
    event7.display_text("Your parents arrive to visit you.. Your mother sees Elsa and Edward kissing on the hall and tells you that she has decided to stay to take care of the business.")
    event8 = Event()
    event8.display_text("(Two days later.... The death of Edward is announced.... He was murdered.... Just a few hours after been named the new CEO of MacArthur Corp) You're hired to find the murderer!")
    event9 = Event()
    event9.display_text("(You receive a call from the head of the police department) Head of the police department: Good afternoon detective! We have a new case for you.. Edward Claythorne was murdered a few hours ago.. I have hired a new assistant for you to help you in the case.. Let me know when you have solved the crime.") 
    event10 = Event()
    user_name = event10.ask_user_name()
    os.system('cls')
    return user_name
    
    
user_name = starting()

##############################################################Engine
class Engine(object):
    global attempts
    menu = Actions()
    while attempts < 3: 
        print(f"Assistant: What do you want to do detective {user_name}?")
        for i, action in enumerate(possible_actions):
            print(f"{i+1}. {action}")
        user_input = input("You: ").lower()
        os.system('cls')
        while "question" not in user_input and "solve" not in user_input and "files" not in user_input and "1" not in user_input and "2" not in user_input and "3" not in user_input: 
            print(f"Assistant: What do you want to do detective {user_name}?")
            for i, action in enumerate(possible_actions):
                print(f"{i+1}. {action}")
            user_input = input("You: ").lower()
            os.system('cls')
        if "question" in user_input or "2" in user_input:
            print("Assistant: Who are we questioning dectective?")
            for i, suspect in enumerate(suspects_again):
                print(f"{i+1}. {suspect.name}.")
            print("(Only write their first name. Don't add extra spaces and be careful with spelling!)")
            user_input = input("You: ").lower() 
            os.system('cls')
            while user_input not in full_list_of_suspects:
                print("Assistant: Sorry, I didn't catch that!. Can you tell me again who are we questioning, detective?")
                for i, suspect in enumerate(suspects_again):
                    print(f"{i+1}. {suspect.name}.")
                print("(Only write their first name. Don't add extra spaces and be careful with spelling!)")
                user_input = input("You: ").lower()
                os.system('cls')
            menu.question_witness(globals()[user_input])
        if "solve" in user_input or "3" in user_input:
            print("Assistant: I knew you will solve it! Who was the murderer?")
            for i, suspect in enumerate(suspects_again):
                print(f"{i+1}. {suspect.name}.")
            print("(Only write their first name. Don't add extra spaces and be careful with spelling!)")
            user_input = input("You: ").lower()
            os.system('cls')
            while user_input not in full_list_of_suspects:
                print("Assistant: I knew you will solve it! But I didnt' catch the name of the murderer, would you be so kind as to repeat it again?")
                for i, suspect in enumerate(suspects_again):
                    print(f"{i+1}. {suspect.name}.")
                print("(Only write their first name. Don't add extra spaces and be careful with spelling!)")
                user_input = input("You: ").lower()
                os.system('cls')
            menu.solve_mystery(globals()[user_input])
        if "files" in user_input or "1" in user_input:
            print("Assistant: Here are all your files. Which one would you like to read? (Write full name with spaces and capital letters")
            for i, file in enumerate(your_files):
                print(f"{i+1}. {file}")
            user_input = input("You: ")
            os.system('cls')
            while user_input not in your_files.keys():
                print("Assistant: Sorry I didn't catch what you just said! Here are all your files. Which one would you like to read? (Write full name with spaces and capital letters")
                for i, file in enumerate(your_files):
                    print(f"{i+1}. {file}")
                user_input = input("You: ")
                os.system('cls')
            for key, val in your_files[user_input].items():
                print(key, ":", val)
            waiting = input("(Press E to exit)")
            os.system('cls')
    if attempts == 3: 
        print_after_user_ready(f"Head of the police department: Detective {user_name}! I'm afraid I cannot let you continue with your investigation.. We are professionals! We cannot allow you keep 'guessing'.. We take our job very seriously! We'll get a new detective for the job! I hope you understand!")
        print("Game over!")
        waiting = input("(Press E to exit)")
        exit("Game over")
            
            
        