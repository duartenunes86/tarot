from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import random
import json

# Additional imports if needed for your script
# from kerykeion import Report, AstrologicalSubject

# Define your tarot descriptions and other variables here
# Descriptions for Major Arcana Tarot Cards

# The Fool
the_fool_description = "The Fool symbolizes new beginnings, adventure, and unlimited potential. Representing a free spirit, this card suggests the onset of a journey, encouraging open-mindedness and spontaneity."

# The Magician
the_magician_description = "The Magician represents manifestation, resourcefulness, and power. This card signifies the ability to utilize one's talents and knowledge to achieve goals, emphasizing action and initiative."

# The High Priestess
the_high_priestess_description = "The High Priestess embodies intuition, mystery, and inner knowledge. She suggests a time to trust your instincts and look beyond the obvious, representing wisdom and depth."

# The Empress
the_empress_description = "The Empress signifies fertility, creativity, and abundance. She is a symbol of nurturing, growth, and maternal care, encouraging you to connect with nature and embrace your creative side."

# The Emperor
the_emperor_description = "The Emperor stands for authority, structure, and control. He embodies leadership and fatherly figures, suggesting a period of asserting dominance and organizing chaos."

# The Hierophant
the_hierophant_description = "The Hierophant symbolizes tradition, conformity, and education. This card represents guidance, spiritual wisdom, and adherence to established social structures."

# The Lovers
the_lovers_description = "The Lovers represent relationships, choices, and moral dilemmas. This card emphasizes the importance of partnerships, harmony, and the tough decisions that come with close relationships."

# The Chariot
the_chariot_description = "The Chariot signifies determination, victory, and overcoming obstacles. It represents a journey, physical or metaphorical, that requires focus and resilience."

# Strength
the_strength_description = "Strength represents courage, persuasion, and inner power. This card suggests a period of overcoming fears and challenges through compassion and inner confidence."

# The Hermit
the_hermit_description = "The Hermit signifies introspection, solitude, and seeking inner wisdom. This card encourages taking time for self-reflection and spiritual exploration."

# Wheel of Fortune
the_wheel_of_fortune_description = "The Wheel of Fortune represents fate, changes, and cycles. It suggests that life is constantly in motion, with events turning in ways that may be unexpected but are always moving forward."

# Justice
the_justice_description = "Justice symbolizes fairness, truth, and the law. This card indicates a time for accountability and decision-making based on ethical principles."

# The Hanged Man
the_hanged_man_description = "The Hanged Man represents sacrifice, release, and new perspectives. It suggests a period of suspension and letting go, leading to a different outlook on life."

# Death
the_death_description = "Death signifies transformation, endings, and new beginnings. This card is about closing one chapter to start another, symbolizing significant change and renewal."

# Temperance
the_temperance_description = "Temperance stands for balance, moderation, and patience. It emphasizes finding middle ground, practicing self-restraint, and blending opposites to create harmony."


the_fool_description = "The Fool symbolizes new beginnings, adventure, and unlimited potential. Representing a free spirit, this card suggests the onset of a journey, encouraging open-mindedness and spontaneity."

# The Magician
the_magician_description = "The Magician represents manifestation, resourcefulness, and power. This card signifies the ability to utilize one's talents and knowledge to achieve goals, emphasizing action and initiative."

# The High Priestess
the_high_priestess_description = "The High Priestess embodies intuition, mystery, and inner knowledge. She suggests a time to trust your instincts and look beyond the obvious, representing wisdom and depth."

# The Empress
the_empress_description = "The Empress signifies fertility, creativity, and abundance. She is a symbol of nurturing, growth, and maternal care, encouraging you to connect with nature and embrace your creative side."

# The Emperor
the_emperor_description = "The Emperor stands for authority, structure, and control. He embodies leadership and fatherly figures, suggesting a period of asserting dominance and organizing chaos."

# The Hierophant
the_hierophant_description = "The Hierophant symbolizes tradition, conformity, and education. This card represents guidance, spiritual wisdom, and adherence to established social structures."

# The Lovers
the_lovers_description = "The Lovers represent relationships, choices, and moral dilemmas. This card emphasizes the importance of partnerships, harmony, and the tough decisions that come with close relationships."

# The Chariot
the_chariot_description = "The Chariot signifies determination, victory, and overcoming obstacles. It represents a journey, physical or metaphorical, that requires focus and resilience."

# Strength
the_strength_description = "Strength represents courage, persuasion, and inner power. This card suggests a period of overcoming fears and challenges through compassion and inner confidence."

# The Hermit
the_hermit_description = "The Hermit signifies introspection, solitude, and seeking inner wisdom. This card encourages taking time for self-reflection and spiritual exploration."

# Wheel of Fortune
the_wheel_of_fortune_description = "The Wheel of Fortune represents fate, changes, and cycles. It suggests that life is constantly in motion, with events turning in ways that may be unexpected but are always moving forward."

# Justice
the_justice_description = "Justice symbolizes fairness, truth, and the law. This card indicates a time for accountability and decision-making based on ethical principles."

# The Hanged Man
the_hanged_man_description = "The Hanged Man represents sacrifice, release, and new perspectives. It suggests a period of suspension and letting go, leading to a different outlook on life."

# Death
the_death_description = "Death signifies transformation, endings, and new beginnings. This card is about closing one chapter to start another, symbolizing significant change and renewal."

# Temperance
the_temperance_description = "Temperance stands for balance, moderation, and patience. It emphasizes finding middle ground, practicing self-restraint, and blending opposites to create harmony."





# Descriptions for Major Arcana Tarot Cards (16-22)

# The Devil
the_devil_description = "The Devil represents bondage, materialism, and ignorance. It suggests being trapped by desires or lower instincts, urging a reassessment of one's attachments and constraints."

# The Tower
the_tower_description = "The Tower signifies sudden upheaval, chaos, and revelation. It represents a dramatic change or destruction that clears the way for new opportunities."

# The Star
the_star_description = "The Star symbolizes hope, faith, and rejuvenation. Following a period of turmoil, this card brings serenity and a sense of calm assurance, promising renewal and healing."

# The Moon
the_moon_description = "The Moon represents illusion, intuition, and uncertainty. It suggests exploring the unknown and trusting one's intuition to navigate through confusion and deception."

# The Sun
the_sun_description = "The Sun signifies success, radiance, and abundance. It brings joy, vitality, and optimism, shining light on the positive aspects of life."

# Judgement
the_judgement_description = "Judgement symbolizes rebirth, inner calling, and absolution. It suggests a time of reflection, self-evaluation, and a decision or realization that can lead to a new phase in life."

# The World
the_world_description = "The World represents completion, accomplishment, and travel. It symbolizes the successful conclusion of a cycle, achievement, and a sense of unity and wholeness."

# Descriptions for Minor Arcana Tarot Cards - Suit of Cups (23-30)

# Ace of Cups
ace_of_cups_description = "The Ace of Cups signifies emotional beginnings, intuition, and creativity. It's a card of new relationships, love, and the potential for emotional fulfillment."

# Two of Cups
two_of_cups_description = "The Two of Cups represents connection, love, and partnership. It suggests a harmonious union or agreement, highlighting mutual respect and understanding."

# Three of Cups
three_of_cups_description = "The Three of Cups symbolizes celebration, friendship, and collaboration. It's a time for rejoicing, socializing, and enjoying the company of others."

# Four of Cups
four_of_cups_description = "The Four of Cups indicates apathy, contemplation, and reevaluation. It suggests dissatisfaction with the external world and the need to look inward for answers."

# Five of Cups
five_of_cups_description = "The Five of Cups represents loss, regret, and disappointment. It focuses on emotional challenges and the importance of learning from past mistakes and grief."

# Six of Cups
six_of_cups_description = "The Six of Cups symbolizes nostalgia, childhood memories, and innocence. It represents looking back at the past with fondness and the comfort of familiar places and faces."

# Seven of Cups
seven_of_cups_description = "The Seven of Cups represents choices, illusions, and fantasy. It suggests the need to make a decision but warns of potential deception or distractions."

# Eight of Cups
eight_of_cups_description = "The Eight of Cups signifies abandonment, withdrawal, and introspection. It indicates leaving something behind to seek deeper meaning and spiritual fulfillment."
def index(request):
    # Your view logic for the index page
    return render(request, 'index.html')

# Descriptions for Minor Arcana Tarot Cards - Suit of Cups (31-36)

# Nine of Cups
nine_of_cups_description = "The Nine of Cups represents contentment, satisfaction, and gratitude. It symbolizes emotional fulfillment and the achievement of heart's desires."

# Ten of Cups
ten_of_cups_description = "The Ten of Cups signifies emotional bliss, happy family life, and harmony. It embodies true happiness and a stable, loving environment."

# Page of Cups
page_of_cups_description = "The Page of Cups symbolizes creativity, curiosity, and the start of emotional experience. It suggests the potential for new feelings or the beginnings of a creative project."

# Knight of Cups
knight_of_cups_description = "The Knight of Cups represents charm, romance, and a 'knight in shining armor'. It symbolizes the arrival of a messenger or an invitation into the realm of emotion and feeling."

# Queen of Cups
queen_of_cups_description = "The Queen of Cups is intuitive, caring, and empathetic. She represents emotional stability and a deep, nurturing understanding of others."

# King of Cups
king_of_cups_description = "The King of Cups embodies wisdom, calmness, and diplomacy. He suggests control over feelings and the ability to balance emotional aspects with intellect."

# Descriptions for Minor Arcana Tarot Cards - Suit of Pentacles (37-50)

# Ace of Pentacles
ace_of_pentacles_description = "The Ace of Pentacles represents new financial opportunities, prosperity, and stability. It suggests the beginning of wealth accumulation and material success."

# Two of Pentacles
two_of_pentacles_description = "The Two of Pentacles symbolizes balance, adaptability, and time management. It represents juggling financial or material priorities and adapting to challenges."

# Three of Pentacles
three_of_pentacles_description = "The Three of Pentacles signifies collaboration, teamwork, and skill. It indicates achieving goals through cooperation, planning, and competency."

# Four of Pentacles
four_of_pentacles_description = "The Four of Pentacles represents security, control, and conservatism. It suggests a focus on financial stability but warns against becoming too materialistic or stingy."

# Five of Pentacles
five_of_pentacles_description = "The Five of Pentacles indicates financial loss, insecurity, and isolation. It represents tough times, yet suggests the need for faith and support."

# Six of Pentacles
six_of_pentacles_description = "The Six of Pentacles symbolizes generosity, charity, and giving. It represents the balance of financial resources, both in terms of giving and receiving aid."

# Seven of Pentacles
seven_of_pentacles_description = "The Seven of Pentacles signifies patience, investment, and long-term planning. It suggests evaluating past efforts and planning future ones for greater success."

# Eight of Pentacles
eight_of_pentacles_description = "The Eight of Pentacles represents dedication, craftsmanship, and skill development. It indicates a time of hard work, commitment, and attention to detail."

# Nine of Pentacles
nine_of_pentacles_description = "The Nine of Pentacles symbolizes luxury, self-sufficiency, and financial independence. It represents the reward for hard work and the enjoyment of the finer things in life."

# Ten of Pentacles
ten_of_pentacles_description = "The Ten of Pentacles signifies wealth, inheritance, and family. It represents financial stability, long-term success, and the foundations of legacy and tradition."

# Descriptions for Minor Arcana Tarot Cards - Suit of Swords (51-64)

# Ace of Swords
ace_of_swords_description = "The Ace of Swords symbolizes a breakthrough, clarity, and sharp intellect. It suggests a time of new ideas, breakthroughs in understanding, or moments of epiphany."

# Two of Swords
two_of_swords_description = "The Two of Swords represents indecision, balance, and a stalemate. It suggests a need for a truce and a time to make a balanced and considered decision."

# Three of Swords
three_of_swords_description = "The Three of Swords signifies heartbreak, loss, and emotional pain. It often points to difficult separations and the need to confront and heal from emotional wounds."

# Four of Swords
four_of_swords_description = "The Four of Swords indicates rest, recovery, and contemplation. It suggests taking a break to rejuvenate and prepare for future challenges."

# Five of Swords
five_of_swords_description = "The Five of Swords represents conflict, tension, and disputes. It warns of the potential for empty victories or the need to consider the cost of winning at all costs."

# Six of Swords
six_of_swords_description = "The Six of Swords signifies transition, change, and moving on. It suggests a journey away from turmoil towards peace, albeit a journey that may be bittersweet."

# Seven of Swords
seven_of_swords_description = "The Seven of Swords symbolizes strategy, evasion, and a stealthy approach. It warns of deception or the need to be tactful and strategic in dealings."

# Eight of Swords
eight_of_swords_description = "The Eight of Swords represents restriction, limitation, and self-imposed constraints. It suggests feeling trapped but encourages seeking ways to break free from constraints."

# Nine of Swords
nine_of_swords_description = "The Nine of Swords signifies anxiety, worry, and fear. It represents a period of mental anguish or stress, urging the need to confront and manage one's fears."

# Ten of Swords
ten_of_swords_description = "The Ten of Swords represents betrayal, loss, and a painful ending. It suggests hitting rock bottom but also implies that things can only improve from here."

# Page of Swords
page_of_swords_description = "The Page of Swords symbolizes curiosity, restlessness, and mental energy. It represents a thirst for knowledge but also warns against gossip or superficial understanding."

# Knight of Swords
knight_of_swords_description = "The Knight of Swords represents ambition, action, and impulsiveness. It suggests charging ahead with energy but warns against hasty or reckless behavior."

# Queen of Swords
queen_of_swords_description = "The Queen of Swords symbolizes independence, unbiased judgment, and direct communication. She represents clarity of thought and straightforwardness in dealings."

# King of Swords
king_of_swords_description = "The King of Swords represents intellect, authority, and ethical leadership. It suggests making decisions based on logic and maintaining moral integrity."

# Descriptions for Minor Arcana Tarot Cards - Suit of Wands (65-78)

# Ace of Wands
ace_of_wands_description = "The Ace of Wands symbolizes inspiration, new opportunities, and potential. It suggests the spark of a new idea or the beginning of an exciting adventure."

# Two of Wands
two_of_wands_description = "The Two of Wands represents planning, future action, and progress. It suggests looking ahead and planning for what is to come, with the world in your hands."

# Three of Wands
three_of_wands_description = "The Three of Wands signifies foresight, expansion, and overseas opportunities. It represents looking ahead to the future and the expansion of horizons."

# Four of Wands
four_of_wands_description = "The Four of Wands symbolizes celebration, harmony, and a milestone. It suggests a time of joy and satisfaction, often marking an important event or rite of passage."

# Five of Wands
five_of_wands_description = "The Five of Wands represents competition, conflict, and struggle. It suggests facing challenges or rivalries but also learning through overcoming these obstacles."

# Six of Wands
six_of_wands_description = "The Six of Wands signifies success, public recognition, and progress. It represents achieving success and receiving accolades for your achievements."

# Seven of Wands
seven_of_wands_description = "The Seven of Wands represents defense, resilience, and standing your ground. It suggests facing challenges confidently and defending your position."

# Eight of Wands
eight_of_wands_description = "The Eight of Wands symbolizes speed, action, and rapid movement. It suggests things moving quickly and a time of fast-paced change."

# Nine of Wands
nine_of_wands_description = "The Nine of Wands symbolizes resilience, persistence, and nearing completion. It represents a final challenge before achieving a goal, urging perseverance."

# Ten of Wands
ten_of_wands_description = "The Ten of Wands signifies burden, responsibility, and hard work. It suggests feeling overwhelmed by obligations but encourages reevaluating your workload."

# Page of Wands
page_of_wands_description = "The Page of Wands represents enthusiasm, exploration, and discovery. It symbolizes a free spirit embarking on an adventure, full of energy and ideas."

# Knight of Wands
knight_of_wands_description = "The Knight of Wands is all about action, adventure, and impulsiveness. He represents a passionate approach to life, but cautions against haste and recklessness."

# Queen of Wands
queen_of_wands_description = "The Queen of Wands symbolizes vibrancy, warmth, and determination. She is a figure of optimism and confidence, encouraging boldness and self-expression."

# King of Wands
king_of_wands_description = "The King of Wands represents visionary leadership, charisma, and daring. He embodies a bold and dynamic approach, inspiring others with his enthusiasm and energy."
page_of_pentacles_description = (
    "The Page of Pentacles represents opportunity, ambition, and practicality. "
    "This card often depicts a young person, standing in a field with a single pentacle in their hands. "
    "They appear thoughtful and focused, symbolizing the early stages of realizing a goal. "
    "This card suggests exploring new opportunities, being studious, and having a desire to learn new skills or knowledge. "
    "It's about the initial steps towards material or career achievements."
)

knight_of_pentacles_description = (
    "The Knight of Pentacles is characterized by dependability, routine, and diligence. "
    "This knight is often shown on a sturdy horse, carefully holding a pentacle. "
    "Unlike other knights, this one is not in a hurry, representing persistence, responsibility, and a methodical approach to achieving goals. "
    "This card suggests a time for hard work, reliability, and sticking to a plan. "
    "It can also indicate a person who is trustworthy and steadfast."
)

queen_of_pentacles_description = (
    "The Queen of Pentacles represents nurturing, practicality, and material comfort. "
    "This card typically shows a queen sitting in a lush, fruitful garden, holding a pentacle. "
    "She is often associated with abundance, financial security, and caring for others. "
    "This queen is practical, down-to-earth, and good at managing resources. "
    "She suggests an approach to life that is grounded, nurturing, and generous, often indicating a person who is a caring provider."
)

king_of_pentacles_description = (
    "The King of Pentacles symbolizes wealth, security, and leadership. "
    "This king is often depicted seated on a throne, surrounded by symbols of material success, holding a pentacle. "
    "He represents mastery over the material realm, being a successful leader, manager, or provider. "
    "The King of Pentacles is a sign of financial stability and security, suggesting a person who is responsible, reliable, and good with money."
)


@csrf_exempt
def run_script(request):
 if request.method == 'POST':
     number = random.randint(1, 78)
     result = ""

     match number:
            case 1:
                result += the_fool_description
            case 2:
                result += the_magician_description
            case 3:
                result += the_high_priestess_description
            case 4:
                result += the_empress_description
            case 5:
                result += the_emperor_description
            case 6:
                result += the_hierophant_description
            case 7:
                result += the_lovers_description
            case 8:
                result += the_chariot_description
            case 9:
                result += the_strength_description
            case 10:
                result += the_hermit_description
            case 11:
                result += the_wheel_of_fortune_description
            case 12:
                result += the_justice_description
            case 13:
                result += the_hanged_man_description
            case 14:
                result += the_death_description
            case 15:
                result += the_temperance_description
            case 16:
                result += the_devil_description
            case 17:
                result += the_tower_description
            case 18:
                result += the_star_description
            case 19:
                result += the_moon_description
            case 20:
                result += the_sun_description
            case 21:
                result += the_judgement_description
            case 22:
                result += the_world_description
            # Minor Arcana: Cups
            case 23:
                result += ace_of_cups_description
            case 24:
                result += two_of_cups_description
            case 25:
                result += three_of_cups_description
            case 26:
                result += four_of_cups_description
            case 27:
                result += five_of_cups_description
            case 28:
                result += six_of_cups_description
            case 29:
                result += seven_of_cups_description
            case 30:
                result += eight_of_cups_description
            case 31:
                result += nine_of_cups_description
            case 32:
                result += ten_of_cups_description
            case 33:
                result += page_of_cups_description
            case 34:
                result += knight_of_cups_description
            case 35:
                result += queen_of_cups_description
            case 36:
                result += king_of_cups_description
            # Minor Arcana: Pentacles
            case 37:
                result += ace_of_pentacles_description
            case 38:
                result += two_of_pentacles_description
            case 39:
                result += three_of_pentacles_description
            case 40:
                result += four_of_pentacles_description
            case 41:
                result += five_of_pentacles_description
            case 42:
                result += six_of_pentacles_description
            case 43:
                result += seven_of_pentacles_description
            case 44:
                result += eight_of_pentacles_description
            case 45:
                result += nine_of_pentacles_description
            case 46:
                result += ten_of_pentacles_description
            case 47:
                result += page_of_pentacles_description
            case 48:
                result += knight_of_pentacles_description
            case 49:
                result += queen_of_pentacles_description
            case 50:
                result += king_of_pentacles_description
            # Minor Arcana: Swords
            case 51:
                result += ace_of_swords_description
            case 52:
                result += two_of_swords_description
            case 53:
                result += three_of_swords_description
            case 54:
                result += four_of_swords_description
            case 55:
                result += five_of_swords_description
            case 56:
                result += six_of_swords_description
            case 57:
                result += seven_of_swords_description
            case 58:
                result += eight_of_swords_description
            case 59:
                result += nine_of_swords_description
            case 60:
                result += ten_of_swords_description
            case 61:
                result += page_of_swords_description
            case 62:
                result += knight_of_swords_description
            case 63:
                result += queen_of_swords_description
            case 64:
                result += king_of_swords_description
            # Minor Arcana: Wands
            case 65:
                result += ace_of_wands_description
            case 66:
                result += two_of_wands_description
            case 67:
                result += three_of_wands_description
            case 68:
                result += four_of_wands_description
            case 69:
                result += five_of_wands_description
            case 70:
                result += six_of_wands_description
            case 71:
                result += seven_of_wands_description
            case 72:
                result += eight_of_wands_description
            case 73:
                result += nine_of_wands_description
            case 74:
                result += ten_of_wands_description
            case 75:
                result += page_of_wands_description
            case 76:
                result += knight_of_wands_description
            case 77:
                result += queen_of_wands_description
            case 78:
                result += king_of_wands_description


     return JsonResponse({'result': result})

 else:
        return JsonResponse({'error': 'Only POST method is accepted'}, status=400)

# Include other view functions if needed
def index(request):
    return render(request, 'index.html')


        