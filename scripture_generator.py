import tkinter as tk
from tkinter import ttk
from random import choice as c
from PIL import Image as I, ImageTk as IT


root = tk.Tk()
root.title("Scripture Generator")
root.minsize(500, 300)
image = I.open("scripgenimage.png")
photo = IT.PhotoImage(image)
root.iconphoto(True, photo)


class Scripture:
    def __init__(self, location, says, meaning):
        self.location = location
        self.says = says
        self.meaning = meaning

scriptures = {
    "uplifting_scriptures": {
        "Psalm 23:1": Scripture(
            "Psalm 23:1",
            "The Lord is my shepherd; I shall not want.",
            "God takes care of me like a good shepherd."
        ),
        "Jeremiah 29:11": Scripture(
            "Jeremiah 29:11",
            "For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope.",
            "God has good plans for me."
        ),
        "Philippians 4:13": Scripture(
            "Philippians 4:13",
            "I can do all things through Christ who strengthens me.",
            "Jesus helps me be strong."
        ),
        "Isaiah 41:10": Scripture(
            "Isaiah 41:10",
            "Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you.",
            "God is with me, so I don’t have to be scared."
        ),
        "John 3:16": Scripture(
            "John 3:16",
            "For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.",
            "God loves me so much He sent Jesus for me."
        ),
        "Romans 8:28": Scripture(
            "Romans 8:28",
            "And we know that for those who love God all things work together for good.",
            "God can turn hard things into good."
        ),
        "Joshua 1:9": Scripture(
            "Joshua 1:9",
            "Be strong and courageous. Do not be frightened, and do not be dismayed, for the Lord your God is with you wherever you go.",
            "God goes with me everywhere."
        ),
        "Psalm 56:3": Scripture(
            "Psalm 56:3",
            "When I am afraid, I put my trust in you.",
            "When I’m scared, I can tell God and trust Him."
        ),
        "Proverbs 3:5-6": Scripture(
            "Proverbs 3:5-6",
            "Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths.",
            "I trust God, and He shows me the right way."
        ),
        "Zephaniah 3:17": Scripture(
            "Zephaniah 3:17",
            "The Lord your God is in your midst, a mighty one who will save; he will rejoice over you with gladness.",
            "God is happy I’m His child and He keeps me safe."
        ),
        "Matthew 11:28": Scripture(
            "Matthew 11:28",
            "Come to me, all who labor and are heavy laden, and I will give you rest.",
            "Jesus gives my heart a rest hug."
        ),
        "Psalm 139:14": Scripture(
            "Psalm 139:14",
            "I praise you, for I am fearfully and wonderfully made.",
            "God made me special and wonderful."
        ),
        "1 Peter 5:7": Scripture(
            "1 Peter 5:7",
            "Casting all your anxieties on him, because he cares for you.",
            "I can tell God my worries; He cares about me."
        ),
        "Psalm 46:1": Scripture(
            "Psalm 46:1",
            "God is our refuge and strength, a very present help in trouble.",
            "God is my safe place and my helper."
        ),
        "John 14:27": Scripture(
            "John 14:27",
            "Peace I leave with you; my peace I give to you… Let not your hearts be troubled, neither let them be afraid.",
            "Jesus gives me calm inside."
        ),
        "Psalm 118:24": Scripture(
            "Psalm 118:24",
            "This is the day that the Lord has made; let us rejoice and be glad in it.",
            "God made today; I can be happy in it."
        ),
        "Romans 15:13": Scripture(
            "Romans 15:13",
            "May the God of hope fill you with all joy and peace in believing.",
            "God fills me with happy hope and quiet peace."
        ),
        "Lamentations 3:22-23": Scripture(
            "Lamentations 3:22-23",
            "The steadfast love of the Lord never ceases; his mercies never come to an end; they are new every morning.",
            "God’s love and kindness start fresh every day."
        ),
        "Psalm 27:1": Scripture(
            "Psalm 27:1",
            "The Lord is my light and my salvation; whom shall I fear?",
            "God is my light and helps me be brave."
        ),
        "Deuteronomy 31:8": Scripture(
            "Deuteronomy 31:8",
            "The Lord goes before you and will be with you. He will never leave you.",
            "God is always with me, even when things are hard."
        ),
        "Psalm 34:18": Scripture(
            "Psalm 34:18",
            "The Lord is near to those who have a broken heart.",
            "God stays close when I feel sad."
        ),
        "Isaiah 40:31": Scripture(
            "Isaiah 40:31",
            "Those who hope in the Lord will renew their strength.",
            "God gives me new strength when I feel tired."
        ),
        "Romans 8:39": Scripture(
            "Romans 8:39",
            "Nothing in all creation can separate us from the love of God.",
            "Nothing can take God's love away from me."
        ),
        "Psalm 121:2": Scripture(
            "Psalm 121:2",
            "My help comes from the Lord, who made heaven and earth.",
            "The God who made everything is my helper."
        ),
        "2 Corinthians 12:9": Scripture(
            "2 Corinthians 12:9",
            "My grace is sufficient for you, for my power is made perfect in weakness.",
            "God helps me even when I feel weak."
        ),
        "Psalm 91:2": Scripture(
            "Psalm 91:2",
            "He is my refuge and my fortress, my God, in whom I trust.",
            "I can trust God when I need protection."
        ),
        "1 John 4:19": Scripture(
            "1 John 4:19",
            "We love because he first loved us.",
            "God loved me first and teaches me to love others."
        ),
        "Psalm 30:5": Scripture(
            "Psalm 30:5",
            "Weeping may stay for the night, but joy comes in the morning.",
            "Sad times do not last forever."
        ),
        "Hebrews 13:5": Scripture(
            "Hebrews 13:5",
            "God has promised never to leave or abandon his people.",
            "God will never leave me alone."
        ),
        "Isaiah 43:2": Scripture(
            "Isaiah 43:2",
            "When you pass through the waters, I will be with you.",
            "God stays with me through difficult times."
        ),
    },
    "teaching_scriptures": {
        "Ephesians 6:1": Scripture(
            "Ephesians 6:1",
            "Children, obey your parents in the Lord, for this is right.",
            "Listening to Mom and Dad makes God happy."
        ),
        "Colossians 3:23": Scripture(
            "Colossians 3:23",
            "Whatever you do, work heartily, as for the Lord and not for men.",
            "Do your best because it makes God glad."
        ),
        "Matthew 7:12": Scripture(
            "Matthew 7:12",
            "So whatever you wish that others would do to you, do also to them.",
            "Treat people the way you want them to treat you."
        ),
        "Proverbs 22:6": Scripture(
            "Proverbs 22:6",
            "Train up a child in the way he should go; even when he is old he will not depart from it.",
            "Learning about God now will help me later too."
        ),
        "James 1:19": Scripture(
            "James 1:19",
            "Let every person be quick to hear, slow to speak, slow to anger.",
            "Listen first, talk kindly, and don’t get mad fast."
        ),
        "Luke 6:31": Scripture(
            "Luke 6:31",
            "And as you wish that others would do to you, do so to them.",
            "Be nice to others like you want them to be nice to you."
        ),
        "Proverbs 15:1": Scripture(
            "Proverbs 15:1",
            "A soft answer turns away wrath, but a harsh word stirs up anger.",
            "Gentle words make peace; mean words cause fights."
        ),
        "Micah 6:8": Scripture(
            "Micah 6:8",
            "He has told you, O man, what is good; and what does the Lord require of you but to do justice, and to love kindness, and to walk humbly with your God?",
            "God wants me to be fair, kind, and humble."
        ),
        "1 Thessalonians 5:16-18": Scripture(
            "1 Thessalonians 5:16-18",
            "Rejoice always, pray without ceasing, give thanks in all circumstances.",
            "Be happy, talk to God, and say thank you all the time."
        ),
        "Proverbs 3:9": Scripture(
            "Proverbs 3:9",
            "Honor the Lord with your wealth and with the firstfruits of all your produce.",
            "Give God the best of what I have first."
        ),
        "Matthew 5:16": Scripture(
            "Matthew 5:16",
            "Let your light shine before others, so that they may see your good works and give glory to your Father who is in heaven.",
            "Do good things so people see God’s love in me."
        ),
        "Proverbs 12:22": Scripture(
            "Proverbs 12:22",
            "The Lord delights in people who are truthful.",
            "God wants me to always tell the truth."
        ),
        "Galatians 5:22-23": Scripture(
            "Galatians 5:22-23",
            "The fruit of the Spirit includes love, joy, peace, patience, kindness, goodness, faithfulness, gentleness, and self-control.",
            "God helps me grow good qualities in my heart."
        ),
        "Proverbs 17:17": Scripture(
            "Proverbs 17:17",
            "A friend loves at all times.",
            "A good friend shows love even when things are hard."
        ),
        "James 4:10": Scripture(
            "James 4:10",
            "Humble yourselves before the Lord, and he will lift you up.",
            "I should be humble instead of thinking I am better than others."
        ),
        "Matthew 5:9": Scripture(
            "Matthew 5:9",
            "Blessed are the peacemakers, for they shall be called children of God.",
            "God wants me to help people get along."
        ),
        "Proverbs 16:24": Scripture(
            "Proverbs 16:24",
            "Gracious words are like a honeycomb, sweet to the soul.",
            "Kind words can make someone feel better."
        ),
        "Luke 16:10": Scripture(
            "Luke 16:10",
            "Whoever is faithful in very little is also faithful in much.",
            "Doing small things responsibly shows I can be trusted."
        ),
        "1 Corinthians 10:31": Scripture(
            "1 Corinthians 10:31",
            "Whatever you do, do all to the glory of God.",
            "I can honor God through the things I do every day."
        ),
        "Proverbs 10:12": Scripture(
            "Proverbs 10:12",
            "Hatred stirs up conflict, but love covers offenses.",
            "Choosing love and forgiveness helps stop arguments."
        ),
        "Romans 12:10": Scripture(
            "Romans 12:10",
            "Love one another with brotherly affection. Outdo one another in showing honor.",
            "I should show love and respect to other people."
        ),
        "Philippians 2:3": Scripture(
            "Philippians 2:3",
            "Do nothing from selfish ambition, but in humility count others more significant than yourselves.",
            "I should think about other people's needs too."
        ),
        "Proverbs 13:20": Scripture(
            "Proverbs 13:20",
            "Whoever walks with the wise becomes wise.",
            "Choosing good friends helps me make good decisions."
        ),
        "James 1:22": Scripture(
            "James 1:22",
            "Be doers of the word, and not hearers only.",
            "God wants me to practice what I learn from the Bible."
        ),
        "Matthew 6:14": Scripture(
            "Matthew 6:14",
            "If you forgive others their trespasses, your heavenly Father will also forgive you.",
            "God teaches me to forgive people who hurt my feelings."
        ),
        "1 Timothy 4:12": Scripture(
            "1 Timothy 4:12",
            "Set an example in speech, conduct, love, faith, and purity.",
            "Even though I am young, I can be a good example."
        ),
        "Proverbs 11:25": Scripture(
            "Proverbs 11:25",
            "Whoever brings blessing will be enriched, and one who waters will himself be watered.",
            "Being generous and helping others brings blessings."
        ),
        "Galatians 6:9": Scripture(
            "Galatians 6:9",
            "Let us not grow weary of doing good.",
            "I should keep doing good things even when it is difficult."
        ),
        "Romans 12:21": Scripture(
            "Romans 12:21",
            "Do not be overcome by evil, but overcome evil with good.",
            "When someone is mean, I can choose to respond with kindness."
        ),
        "Ephesians 4:32": Scripture(
            "Ephesians 4:32",
            "Be kind to one another, tenderhearted, forgiving one another.",
            "Be kind and forgive people when they make mistakes."
        ),
    },
    "prayer_scriptures": {
        "Philippians 4:6": Scripture(
            "Philippians 4:6",
            "Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God.",
            "Don’t worry—talk to God about everything."
        ),
        "1 Thessalonians 5:17": Scripture(
            "1 Thessalonians 5:17",
            "Pray without ceasing.",
            "I can talk to God all the time."
        ),
        "Matthew 6:9-13": Scripture(
            "Matthew 6:9-13",
            "Pray then like this: 'Our Father in heaven, hallowed be your name...'",
            "Jesus showed me how to pray to God like a loving Father."
        ),
        "Mark 11:24": Scripture(
            "Mark 11:24",
            "Therefore I tell you, whatever you ask in prayer, believe that you have received it, and it will be yours.",
            "Believe God hears me when I pray."
        ),
        "Psalm 145:18": Scripture(
            "Psalm 145:18",
            "The Lord is near to all who call on him, to all who call on him in truth.",
            "God comes close when I pray to Him."
        ),
        "Jeremiah 29:12": Scripture(
            "Jeremiah 29:12",
            "Then you will call upon me and come and pray to me, and I will hear you.",
            "When I pray, God listens."
        ),
        "James 5:16": Scripture(
            "James 5:16",
            "The prayer of a righteous person has great power as it is working.",
            "Prayers are powerful when I love God."
        ),
        "Matthew 21:22": Scripture(
            "Matthew 21:22",
            "And whatever you ask in prayer, you will receive, if you have faith.",
            "Pray and believe—God can answer."
        ),
        "Colossians 4:2": Scripture(
            "Colossians 4:2",
            "Continue steadfastly in prayer, being watchful in it with thanksgiving.",
            "Keep praying and always say thank you to God."
        ),
        "Psalm 17:6": Scripture(
            "Psalm 17:6",
            "I call upon you, for you will answer me, O God; incline your ear to me; hear my words.",
            "God listens when I call out to Him."
        ),
        "Matthew 7:7": Scripture(
            "Matthew 7:7",
            "Ask, and it will be given to you; seek, and you will find; knock, and it will be opened to you.",
            "God wants me to come to Him and ask for help."
        ),
        "John 14:13": Scripture(
            "John 14:13",
            "Whatever you ask in my name, this I will do, that the Father may be glorified in the Son.",
            "Jesus teaches me to pray in His name."
        ),
        "1 John 5:14": Scripture(
            "1 John 5:14",
            "If we ask anything according to his will, he hears us.",
            "God listens when I pray according to His will."
        ),
        "Romans 12:12": Scripture(
            "Romans 12:12",
            "Rejoice in hope, be patient in tribulation, be constant in prayer.",
            "I can keep praying even when life is difficult."
        ),
        "Psalm 55:17": Scripture(
            "Psalm 55:17",
            "Evening and morning and at noon I utter my complaint and moan, and he hears my voice.",
            "I can talk to God at any time of day."
        ),
        "Luke 11:9": Scripture(
            "Luke 11:9",
            "Ask, and it will be given to you; seek, and you will find.",
            "God encourages me to keep coming to Him."
        ),
        "James 1:5": Scripture(
            "James 1:5",
            "If any of you lacks wisdom, let him ask God, who gives generously to all.",
            "I can ask God to help me make wise decisions."
        ),
        "Psalm 66:19": Scripture(
            "Psalm 66:19",
            "But truly God has listened; he has attended to the voice of my prayer.",
            "God hears me when I talk to Him."
        ),
        "Matthew 6:6": Scripture(
            "Matthew 6:6",
            "When you pray, go into your room and shut the door and pray to your Father who is in secret.",
            "I can spend quiet time alone talking with God."
        ),
        "Psalm 86:7": Scripture(
            "Psalm 86:7",
            "In the day of my trouble I call upon you, for you answer me.",
            "When I have problems, I can ask God for help."
        ),
        "1 Peter 3:12": Scripture(
            "1 Peter 3:12",
            "The eyes of the Lord are on the righteous, and his ears are open to their prayer.",
            "God pays attention when His people pray."
        ),
        "Hebrews 4:16": Scripture(
            "Hebrews 4:16",
            "Let us then with confidence draw near to the throne of grace.",
            "I can come to God without being afraid."
        ),
        "Psalm 5:3": Scripture(
            "Psalm 5:3",
            "O Lord, in the morning you hear my voice; in the morning I prepare a sacrifice for you and watch.",
            "I can begin each morning by talking to God."
        ),
        "Luke 18:1": Scripture(
            "Luke 18:1",
            "Jesus told them a parable to the effect that they ought always to pray and not lose heart.",
            "Jesus wants me to keep praying and never give up."
        ),
        "Jeremiah 33:3": Scripture(
            "Jeremiah 33:3",
            "Call to me and I will answer you, and will tell you great and hidden things that you have not known.",
            "God invites me to talk to Him and learn from Him."
        ),
        "Psalm 141:2": Scripture(
            "Psalm 141:2",
            "Let my prayer be counted as incense before you, and the lifting up of my hands as the evening sacrifice.",
            "My prayers are a special gift I can offer to God."
        ),
        "Ephesians 6:18": Scripture(
            "Ephesians 6:18",
            "Praying at all times in the Spirit, with all prayer and supplication.",
            "I can pray throughout my day and pray for other people."
        ),
        "1 Timothy 2:1": Scripture(
            "1 Timothy 2:1",
            "I urge that supplications, prayers, intercessions, and thanksgivings be made for all people.",
            "God wants me to pray for everyone, not just myself."
        ),
        "Psalm 102:17": Scripture(
            "Psalm 102:17",
            "He regards the prayer of the destitute and does not despise their prayer.",
            "God listens to people who feel helpless or alone."
        ),
        "Jude 1:20": Scripture(
            "Jude 1:20",
            "Building yourselves up in your most holy faith and praying in the Holy Spirit.",
            "Prayer helps me grow stronger in my faith."
        ),
    }
}

scrip_values = [key.replace("_scriptures", "").capitalize() for key in scriptures]


def scrip_cat_select():
    cat = category_select.get()
    if cat == "Uplifting":
        return scriptures["uplifting_scriptures"]
    elif cat == "Teaching":
        return scriptures["teaching_scriptures"]
    elif cat == "Prayer":
        return scriptures["prayer_scriptures"]
    else:
        return

def generate_scripture():
    scripture = scrip_cat_select()
    if not scripture:
        return
    scr = c(list(scripture.values()))
    verse = scr.location
    scripture = scr.says
    meaning = scr.meaning

    verse_label.config(text=verse)
    scripture_label.config(text=scripture)
    meaning_label.config(text=meaning)





category_select = ttk.Combobox(root, values=scrip_values, state="readonly")
category_select.pack(padx=10, pady=10)
category_select.set(scrip_values[0])

scrip_frame = tk.Frame(root)
scrip_frame.pack(padx=10, pady=10)

verse_labelframe = tk.LabelFrame(scrip_frame, text="Verse:")
verse_labelframe.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

verse_label = tk.Label(verse_labelframe, anchor="center")
verse_label.pack(fill='x', padx=5, pady=5)

scripture_labelframe = tk.LabelFrame(scrip_frame, text="Scripture:")
scripture_labelframe.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

scripture_label = tk.Label(scripture_labelframe, justify='left', wraplength=220)
scripture_label.pack(padx=5, pady=5)

meaning_labelframe = tk.LabelFrame(scrip_frame, text="Meaning:")
meaning_labelframe.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

meaning_label = tk.Label(meaning_labelframe, justify='left', wraplength=220)
meaning_label.pack(fill="both", padx=5, pady=5)

generate_scrip_button = tk.Button(root, text="Generate", command=generate_scripture)
generate_scrip_button.pack(padx=10, pady=10)

root.mainloop()
