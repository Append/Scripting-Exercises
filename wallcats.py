#yolo 
#cat facts script

import time
import random
import subprocess

cat = ["Both humans and cats have identical regions in the brain responsible for emotion.",
"A cat's brain is more similar to a man's brain than that of a dog.",
"A cat has more bones than a human; humans have 206, but the cat has 230 (some cites list 245 bones, and state that bones may fuse together as the cat ages).",
"Cats have 30 vertebrae (humans have 33 vertebrae during early development; 26 after the sacral and coccygeal regions fuse)",
"The cat's clavicle, or collarbone, does not connect with other bones but is buried in the muscles of the shoulder region. This lack of a functioning collarbone allows them to fit through any opening the size of their head.",
"The cat has 500 skeletal muscles (humans have 650).",
"Cats have 32 muscles that control the outer ear (compared to human's 6 muscles each). A cat can rotate its ears independently 180 degrees, and can turn in the direction of sound 10 times faster than those of the best watchdog.",
"Cats' hearing is much more sensitive than humans and dogs.",
"Cats' hearing stops at 65 khz (kilohertz); humans' hearing stops at 20 khz.",
"A cat sees about 6 times better than a human at night, and needs 1/6 the amount of of light that a human does - it has a layer of extra reflecting cells which absorb light.",
"Recent studies have shown that cats can see blue and green. There is disagreement as to whether they can see red.",
"A cat's field of vision is about 200 degrees.",
"Unlike humans, cats do not need to blink their eyes on a regular basis to keep their eyes lubricated.",
"Blue-eyed, pure white cats are frequently deaf.",
"It may take as long as 2 weeks for a kitten to be able to hear well.  Their eyes usually open between 7 and 10 days, but sometimes it happens in as little as 2 days.",
"Cats can judge within 3 inches the precise location of a sound being made 1 yard away.",
"Cats can be right-pawed or left-pawed.",
"A cat cannot see directly under its nose.",
"Almost 10%% of a cat's bones are in its tail, and the tail is used to maintain balance.",
"The domestic cat is the only species able to hold its tail vertically while walking. You can also learn about your cat's present state of mind by observing the posture of his tail.",
"If a cat is frightened, the hair stands up fairly evenly all over the body; when the cat is threatened or is ready to attack, the hair stands up only in a narrow band along the spine and tail.",
"A cat has approximately 60 to 80 million olfactory cells (a human has between 5 and 20 million).",
"Cats have a special scent organ located in the roof of their mouth, called the Jacobson's organ. It analyzes smells - and is the reason why you will sometimes see your cat sneer (called the flehmen response or flehming) when they encounter a strong odor.",
"Cats dislike citrus scent.",
"A cat has a total of 24 whiskers, 4 rows of whiskers on each side. The upper two rows can move independently of the bottom two rows. ",
"Cats have 30 teeth (12 incisors, 10 premolars, 4 canines, and 4 molars), while dogs have 42. Kittens have baby teeth, which are replaced by permanent teeth around the age of 7 months.",
"A cat's jaw has only up and down motion; it does not have any lateral, side to side motion, like dogs and humans.",  
"A cat's tongue has tiny barbs on it.",
"Cats lap liquid from the underside of their tongue, not from the top.",
"Cats purr at the same frequency as an idling diesel engine, about 26 cycles per second.",
"Domestic cats purr both when inhaling and when exhaling.",
"The cat's front paw has 5 toes, but the back paws have 4. Some cats are born with as many as 7 front toes and extra back toes (polydactl).",
"Cats walk on their toes.",
"A domestic cat can sprint at about 31 miles per hour.",
"A kitten will typically weigh about 3 ounces at birth.  The typical male housecat will weigh between  7 and 9 pounds, slightly less for female housecats.",
"Cats take between 20-40 breaths per minute.",
"Normal body temperature for a cat is 102 degrees F.",
"A cat's normal pulse is 140-240 beats per minute, with an average of 195.",
"Cat's urine glows under a black light.",
"Cats lose almost as much fluid in the saliva while grooming themselves as they do through urination.",
"A cat has two vocal chords, and can make over 100 sounds.",
"Miacis, the primitive ancestor of cats, was a small, tree-living creature of the late Eocene period, some 45 to 50 million years ago.",
"Phoenician cargo ships are thought to have brought the first domesticated cats to Europe in about 900 BC.",
"The first true cats came into existence about 12 million years ago and were the Proailurus.",
"Experts traditionally thought that the Egyptians were the first to domesticate the cat, some 3,600 years ago.  But recent genetic and archaeological discoveries indicate that cat domestication began in the Fertile Crescent, perhaps around 10,000 years ago, when agriculture was getting under way. (per Scientific American, 6/10/2009)",
"Ancient Egyptian family members shaved their eyebrows in mourning when the family cat died.",
"In Siam, the cat was so revered that one rode in a chariot at the head of a parade celebrating the new king.",
"The Pilgrims were the first to introduce cats to North America.",
"The first breeding pair of Siamese cats arrived in England in 1884.",
"The first formal cat show was held in England in 1871; in America, in 1895.",
"The Maine Coon cat is America's only natural breed of domestic feline. It is 4 to 5 times larger than the Singapura, the smallest breed of cat.",
"There are approximately 100 breeds of cat.",
"The life expectancy of cats has nearly doubled since 1930 - from 8 to 16 years.",
"Cats have been domesticated for half as long as dogs have been."]


while True:
  x = random.choice(cat)
	print(x)
  #subprocess.check_call(["echo", x, "| write username[Cat Facts!]"])
  #add more calls to things like email lists
	time.sleep(3600)
