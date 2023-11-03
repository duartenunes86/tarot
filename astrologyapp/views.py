from django.http import HttpResponse
from kerykeion import Report,AstrologicalSubject
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    # Your view logic here
    return render(request, 'index.html')

def run_script(request):
    # Place your Python script logic here

    # Import the main class for creating a kerykeion instance:
 if request.method == 'POST':
        data = json.loads(request.body)
        day = data['day']
        month = data['month']
        year = data['year']
        hour = data['hour']
        minutes = data['minutes']
        year = int(year)
        month = int(month)
        day = int(day)
        hour = int(hour)
        minutes = int(minutes)

# Create a kerykeion instance:
# Args: Name, year, month, day, hour, minuts, city, nation(optional)
 kanye = AstrologicalSubject("Kanye", year, month, day, hour, minutes, "Portugal")

# Get the information about the sun in the chart:
# (The position of the planets always starts at 0)
 print(kanye.sun)

#> {'name': 'Sun', 'quality': 'Mutable', 'element': 'Air', 'sign': 'Gem', 'sign_num': 2, 'pos': 17.598992059774275, 'abs_pos': 77.59899205977428, 'emoji': '♊️', 'house': '12th House', 'retrograde': False}

# Get information about the first house:
 
 rising_sco = "You tend to be reticent, introverted, enigmatic, and occasionally challenging to fathom. Those around you observe your profound emotions and feelings and ponder how to engage you in conversation. You possess a tenacious and resilient spirit, ready to fiercely defend any stance you hold dear. When provoked or upset, you exhibit resourcefulness and formidable determination. You relish a life on the cutting edge, where experiences must be lived with utmost intensity. Your courage is evident, as you're willing to take calculated risks. Though easily wounded by the words or actions of others, you may respond with cutting sarcasm. Your sensitivity and inquisitiveness drive your interest in the deeper mysteries of human psychology. Once you become captivated by a subject, you pursue it with unwavering zeal."
 rising_lib = "You possess a striking allure and enjoy widespread popularity. Your charm is a potent tool that helps you achieve your desires and keeps others from harboring resentment. \"Maintaining peace and harmony at any cost\" is your guiding principle. You make consistent efforts to alleviate or superficially conceal any physical imperfections or conflicts between individuals. Your fashion sense is characterized by elegance rather than gaudiness, and you typically exhibit good taste in music, art, and literature. Yet, be cautious of compromising your values in your quest to always be agreeable. While you can be somewhat of a social butterfly and occasionally show signs of vanity and laziness, for the most part, you are gracious and affectionate. Your refined and aristocratic demeanor serves as an example for others to follow."
 rising_vir = "You often come across as reserved and timid, not one to assert yourself readily. You're exceptionally critical of how you come across to others. Even though you may perceive yourself as uninteresting and lacking sparkle, you are, in fact, softly spoken, orderly, tidy, and quite likable. Your pursuit of perfection is evident, accompanied by high standards. At times, you may be blunt in pointing out the flaws in others. Your approach is highly practical, efficient, and purpose-driven. Your appearance and demeanor convey your desire to appear poised, sensible, and reserved. You maintain a straightforward, no-nonsense attitude in your interactions with others. Laziness and self-indulgence have no place in your life, as you are deeply committed to a strong work ethic."
 rising_leo = "You thrive on being the center of attention and aim to project strength, confidence, and dominance. Pride is a significant part of your personality, at times bordering on vanity. Even when chaos surrounds you, you maintain a polished and composed appearance. Dignity and honor hold great importance for you, and you relish the perks of leadership but might shy away from its responsibilities. You're deeply idealistic but can also be unyielding in your views. You hold others in high regard when they exhibit integrity, although wealth, power, and influence can also catch your eye. Your preference is for opulent and sophisticated surroundings and possessions, which you'll acquire within your means. Physically, you leave a striking impression. At your best, you exude a regal and charismatic presence. It's worth considering toning down the need to show off."
 rising_can = "You possess a high degree of sensitivity by nature and find comfort in your familiar surroundings. Your approach is cautious and conservative, making changes in your life a slow and deliberate process, if you decide to make them at all. You tend to keep your guard up with strangers and don't readily open up to them. However, when it comes to friendships, you are exceptionally loyal – once you establish trust, it endures for a lifetime. Your early family life, including your mother and the home you grew up in, holds great significance to you. Sentimentality is a hallmark of your personality. Your behavior depends on your self-confidence level. When secure, you are gentle, generous, and protective of others' needs. But when feeling insecure or threatened, you become overly sensitive to criticism, and your demeanor turns shy, withdrawn, and moody. A deep-seated need for security, particularly in the form of love, nurturing, and protection, is a strong driving force in your life."
 rising_gem = "You possess an innate restlessness and a strong desire for activity. Meeting new people, exploring different places, and engaging in various activities are your natural tendencies. Staying in one place is a challenge, as you constantly seek movement. To keep your mind engaged, you thrive when involved in multiple projects simultaneously. Reading books, writing letters, and engaging in constant conversation are activities you genuinely enjoy. Your appearance suggests agelessness, often making you appear much younger than your actual age. Your adaptability and inquisitiveness drive you to remain open to new ideas and experiences. You can be described as a \"jack-of-all-trades\" due to your liveliness and versatility. Given your high nervous tension, engaging in athletic activities is an effective way to release your surplus energy. However, be cautious of your tendency to skim the surface of experiences – try to delve deeper and absorb things at a more profound level."
 rising_tau = "You possess a calm and deliberate nature, disliking rushed or hasty actions. Practicality is your guiding principle, as you insist that every effort should have a purpose. You exhibit patience, persistence, and unwavering determination, but your stubbornness is a formidable trait – you cannot be easily swayed or pressured. Outwardly, you project self-assuredness, concealing inner tension and turmoil. Your presence radiates a warm, friendly charm and down-to-earth appeal. You have a preference for comfortable surroundings and the finer things in life. However, be cautious of potential self-indulgence. There are times when you may seem sluggish and challenging to motivate. Overcoming inertia poses a consistent challenge, and since you're not naturally inclined to initiate action, external stimuli often become necessary to set you in motion."
 rising_ari = "You're a free spirit who always aims to be the leader in whatever you undertake. Your energy, assertiveness, and activity levels are remarkably high, and you have a strong inclination to have things go your way. Even if you may feel inner calm and serenity, your outward demeanor doesn't reflect that – you tend to approach everything at full throttle, with a \"go big or go home\" attitude. You excel as a competitor but face challenges when it comes to cooperation – learning to handle losses gracefully is an area for improvement. Your self-confidence, ambition, and passion emit a contagious positive energy. You're known for your straightforward and direct communication style, although at times, you may come across as unfeeling and tactless, especially when met with resistance. While you fiercely fight for your beliefs, your inclination to act before thinking can sometimes lead to regrettable consequences."
 rising_pis = "You possess a high sensitivity to your environment, often absorbing the emotions of those around you. It's advisable to steer clear of negative individuals because your empathetic nature can lead you to adopt their negativity. As an idealist, you seek to believe in something beyond your everyday existence. You're a dreamer who relishes escaping into a world of your own making. This quality makes you known for the richness of your imagination, and it would be beneficial to share your inner visions with others. Your inherent self-sacrificing tendencies are noteworthy, but caution is needed to prevent others from overly relying on you, and vice versa. It's essential to grant yourself moments to live for your own sake – you deserve it. There's no need for envy towards those who exhibit more assertiveness; your gentle charity and genuine humility are truly remarkable qualities. (Note: The mention of \"on the tenth house cusp (MIDHEAVEN)\" at the end seems unrelated to the rest of the description.)"
 rising_aqu = "You have a penchant for embracing new ideas and concepts, yet you prefer to explore them independently – persuading you to change your mind isn't a simple task. You're known for forming your own opinions, and once you do, you often seek to convince others of their correctness. It might be beneficial to cultivate greater tolerance for the views of others. You hold a deep and enduring fascination with science, mathematics, and the significant social issues of the day. You exhibit strong empathy for the underprivileged, and equality is a cause you champion passionately. You expect fairness from those in positions of authority. Your intellectual nature takes precedence, and understanding emotions and emotional individuals can be a challenge for you. Your reputation is one of being composed, detached, and objective, often exuding a calm and cool demeanor."
 rising_cap = "You have a practical and reserved nature but are highly ambitious and value success. In your younger years, you may have appeared older and very serious, but as you mature, you tend to lighten up and become more relaxed. You tend to hold a solemn view of the world, considering it a challenging place to navigate. You often find yourself envious of those who seem to have an easier life than you do, and you may struggle to relax and enjoy leisure. It's crucial that you received substantial support from your parents during your childhood to avoid feeling isolated as an adult. You possess a solid, down-to-earth sense of humor that serves as a source of strength during tough times. Overall, you are purpose-driven, determined, hardworking, grounded in reality, and take your responsibilities seriously."
 rising_sag = "You are renowned for your openness, honesty, and outgoing nature. Occasionally, though, your straightforwardness may come across as blunt and indiscreet. It's important for others to learn not to take everything you say personally, as your intentions are generally not harmful. You prefer to lead a simple and uncomplicated life, disliking social formalities that can hinder genuine communication. You possess abundant energy and tend to become restless if you feel confined. Your need for freedom to make your own choices is paramount; being self-directed is essential, as you feel anxious when trapped. Your high energy levels lead you to enjoy the outdoors, and you're likely drawn to physical activities and sports that allow you to expend some of that excess energy. You're highly sociable, and your natural enthusiasm brings life to any social gathering."
 sco = "Naturally intense and intricate, your emotional reactions to situations are exceptionally strong. Expressing your feelings can be quite challenging, leading to a tendency for quiet contemplation and deep introspection. While you rarely display overt anger, when you do, it is a fiery and unrelenting force. When you invest emotionally, your commitment is unwavering, and you seek profound and meaningful relationships, dismissing superficial or casual connections. Challenges are taken as personal provocations, often leading to a vengeful response. You hold a profound fascination for mysteries and the supernatural, making you an excellent detective who delves into the core of problems and relishes understanding the inner workings of others. Your reputation is that of a strong-willed, powerful, and highly persistent individual."
 lib = "Highly sociable, you relish the company of others and actively avoid solitude. Your nature is characterized by warmth and affection, as you consistently make an effort to endear yourself to those around you. Averse to ugliness, you find it essential to be surrounded by beauty and harmony in your life. Your preference extends to fine attire, an attractive home, and pleasant environments in any setting. Your refined taste also encompasses music and art. However, you occasionally grapple with indecision, often wavering and hesitating when confronted with choices, as you possess the unique ability to see both sides of any issue. This quality, though, lends you remarkable fairness and trustworthiness in resolving disputes. Your primary challenge lies in maximizing the potential of one-on-one interactions."
 vir = "Inherently cautious and exceedingly meticulous, your utmost priority is maintaining tidiness and organization. You adhere rigorously to high standards of living and behavior, and you expect the same level of diligence from everyone you interact with. Sometimes, your meticulousness can border on being overly critical, and you tend to nitpick. You possess excellent practical skills and are adept with various tools. Hygiene, cleanliness, and personal health matters are subjects of great concern for you. Interestingly, your health is likely in better shape than you might believe, so there's no need for excessive worry. You exhibit an extremely methodical and analytical approach to tasks, making you a perfectionist who excels at executing intricate and precise operations. However, on occasion, your intense focus on details may cause you to lose sight of the broader picture."
 leo = "More than a bit of a showoff, you love to be the center of attention! But others do not usually mind because they tend to enjoy your genuine warmth and affection. Very spirited and willful, proud and self-important at times, you demand your own way. You are quite honest, however, and the respect of others is very important to you. You never compromise yourself and you pursue your goals with persistence and dedication. Your regal presence and demeanor draws you to positions of leadership and authority. But beware of being overly hardheaded, domineering, ostentatious or patronizing or you will lose the goodwill and admiration that you enjoy. Very theatrical, you live life on a grand scale wherever and whenever possible. Your strength and energy vitalizes those who come in contact with you. "
 can = "Highly in tune with your emotions and sensitive to the vibes around you, you possess an intuitive understanding of the emotional atmosphere. Your nature is characterized by generosity, love, and care, but you extend these qualities primarily when your own emotional needs for support, love, and security have been fulfilled. If these needs go unmet, you tend to withdraw into yourself, becoming insecure and self-focused. Your sense of security is deeply tied to your home and family, particularly your mother or a significant maternal figure from your early life. Consequently, these elements assume a paramount role in your life. Your sentimental nature results in vivid and long-lasting memories of the past. Regardless of how well-adjusted you may be, you'll always require a private, tranquil space to find inner peace. Providing nourishment to others brings you significant joy, and you'd thrive in a large family setting."
 gem = "You possess a sharp, nimble, and alert intellect, but your attention span is exceptionally brief. Your inclination leans toward the vibrant and ever-changing facets of life, while you tend to steer clear of deep and intimate emotional connections, and may even harbor some fear of them. Consequently, you revel in travel, sightseeing, and a generally dynamic lifestyle. Monotony and stagnation can leave you feeling unenthusiastic, but your enthusiasm is rekindled when presented with fresh ideas. You're a talkative and inquisitive individual with a playful disposition, enjoying practical jokes and games. Your moods shift rapidly and frequently, and you exude restlessness, constantly seeking movement. Your reputation is one of versatility and adaptability, and your vivacious nature brings life to any social gathering."
 tau = "You are renowned for your patience, deliberate pace, and meticulous approach – savoring enjoyable moments is a true pleasure for you. Comfort, ease, and a warm environment are not just preferences but necessities. However, you should be cautious about the inclination to become overly content and complacent, as well as the temptation to overindulge, especially in sweets. For your personal growth and development, you actually need challenging situations, even though you tend to avoid them. Your affectionate, even-tempered nature makes it rare for you to become angry, but when you do, forgiveness comes slowly, and time is required for your calm demeanor to return. You place a strong emphasis on tangible, real-world results and find abstract concepts challenging to grasp. Your artistic inclinations are prominent, and your hands are skillful at molding and shaping things. You exude a physical, earthy sensuality that others often find highly alluring."
 ari = "By nature, you exude a tremendous amount of energy and a lively spirit. Your independence is a defining characteristic – you always strive to be the first in all your endeavors and willingly embrace risks. You're the type of person who fearlessly dives into uncharted territory. You excel at initiating new projects, but your Achilles' heel is following through to completion. While you make for an enthusiastic leader, being a follower doesn't come naturally to you. Your temper can flare quickly, but you also cool down rapidly, often regretting words spoken in haste. One of your standout qualities is your simplicity and directness; you are straightforward and honest. It's essential, however, to exercise caution to avoid hurting others' feelings. Your unwavering drive to be competitive, even at all costs, may occasionally invite resistance from others. As long as you maintain your typical sunny disposition, this shouldn't pose a significant problem for you."
 pis = "Exceptionally sensitive and emotionally attuned, you soak up the feelings of those around you, whether they're positive or negative, much like a sponge. Your emotional vulnerability makes you prone to getting easily upset and shedding tears readily. You shine when you can arrange your surroundings to include positive and cheerful individuals. Your innate helpfulness and understanding of others' needs are remarkable qualities. However, this can sometimes work against you, as you have a tendency to be overly accommodating to anyone in need. Naturally shy, you possess a dreamy and romantic disposition. You take pleasure in escaping into your own private realm of fantasies. It's important to exercise caution not to become completely lost in this world of dreams. Trust your intuitions, as you may have a heightened psychic sensitivity."
 aqu = "You have a tendency to grow weary of the status quo and are generally receptive to new concepts and experiences. An individualist and a free spirit, your friends hold significant value for you as long as they don't attempt to restrict you by imposing excessive emotional demands. Your thoughts often diverge from the mainstream, and you carry a touch of eccentricity, though your opinions don't always change readily. In fact, you can display a fair amount of stubbornness on occasion. Your approach is highly fair-minded when addressing broader groups or broad-scale issues, but you may not always be emotionally attuned to individual needs. You possess an exceptionally objective perspective, coupled with keen powers of observation, which qualify you for studying technical and intricate subjects, such as science, computers, or even astrology."
 cap = "You possess an exceedingly serious and mature disposition, readily embracing responsibilities and fulfilling them willingly. Others naturally expect you to be diligent as a matter of course. You tend to feel frustration when individuals receive rewards without putting in nearly as much effort as you do. Your inherent nature is goal-oriented, and you're a dedicated worker who takes pride in the tangible results of your labor. You often exhibit \"tunnel-vision,\" allowing you to block out distractions that might divert others' attention, enabling you to concentrate entirely on the task at hand. This quality makes you an excellent choice for managing or administering ongoing projects, as you approach them with practicality and efficiency. While you may not be a speedy worker, your thoroughness compensates for it. Your reputation is built on total persistence, unyielding determination, and relentless pursuit of your objectives."
 sag = "You are incredibly fun-loving, spirited, and overflowing with physical energy that seeks an outlet. Consequently, exercise and sports hold great importance in your life. You're quite sociable and relish the company of others, but you tend to steer clear of emotionally constricting or intimate relationships.You exhibit a constant curiosity about life's broader aspects, although you can occasionally be careless and hasty when it comes to details, often jumping to conclusions before gathering all the facts. Your enthusiasm for reading is boundless, especially when a subject piques your interest. You are renowned for your idealism, generosity, sociability, cheerfulness, and an inherently positive outlook on life."
#> {'name': 'First_House', 'quality': 'Cardinal', 'element': 'Water', 'sign': 'Can', 'sign_num': 3, 'pos': 17.995779673209114, 'abs_pos': 107.99577967320911, 'emoji': '♋️'}

# Get element of the moon sign:

 report = Report(kanye)
 result=""

 match kanye.first_house.sign:
    case "Sco":
         result+=rising_sco
    case "Lib":
         result+=rising_lib
    case "Vir":
         result+=rising_vir
    case "Leo":
         result+=rising_leo 
    case "Can":
         result+=rising_can
    case "Gem":
         result+=rising_gem 
    case "Tau":
         result+=rising_tau
    case "Ari":
         result+=rising_ari
    case "Pis":
         result+=rising_pis
    case "Aqu":
         result+=rising_aqu
    case "Cap":
         result+=rising_cap
    case "Sag":
         result+=rising_sag
    case _:
          print("")
 match kanye.planets_list[0].sign:
    case "Sco":
         print(sco)
    case "Lib":
         print(lib)
    case "Vir":
         print(vir)
    case "Leo":
         print(leo) 
    case "Can":
         print(can)  
    case "Gem":
         print(gem)   
    case "Tau":
         print(tau)
    case "Ari":
         print(ari)
    case "Pis":
         print(pis)
    case "Aqu":
         print(aqu)
    case "Cap":
         print(cap)
    case "Sag":
         print(sag)
    case _:
          print("")
        
 return JsonResponse({'result': result})