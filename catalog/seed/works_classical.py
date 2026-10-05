"""Works from Antiquity to the Renaissance."""


def W(slug, title, author, year, kind, lang, pages, difficulty, topics, summary, description, ideas,
      approx=False, original="", pd=False, featured=False):
    return dict(
        slug=slug, title=title, author=author, year=year, kind=kind, lang=lang, pages=pages, difficulty=difficulty,
        topics=topics, summary=summary, description=description, ideas=ideas, approx=approx, original=original,
        pd=pd, featured=featured,
    )


WORKS_CLASSICAL = [
    W("tao-te-ching", "Tao Te Ching", "laozi", -400, "poem", "Classical Chinese", 100, 2,
      ["metaphysics", "ethics", "political-philosophy"],
      "Eighty-one short poetic chapters on the Tao—the nameless Way of things—and the art of living and ruling "
      "without forcing.",
      "Barely five thousand characters long, the Tao Te Ching ('Classic of the Way and Virtue') opens by warning "
      "that the Tao that can be spoken is not the eternal Tao. Through paradox and image—water that overcomes the "
      "hard, the empty hub that makes a wheel useful—it counsels humility, simplicity, softness and wu wei, "
      "effortless action in harmony with nature. Addressed partly to rulers, it advises governing a great state "
      "'as you would cook a small fish': lightly.",
      ["The Tao is the nameless source and pattern of all things, beyond words.",
       "Wu wei: act without forcing; the soft and yielding overcome the hard.",
       "The best rulers are barely noticed; heavy-handed government breeds disorder."],
      approx=True, original="道德經 (Dàodé jīng)", pd=True, featured=True),
    W("analects", "The Analects", "confucius", -400, "aphorisms", "Classical Chinese", 160, 2,
      ["ethics", "political-philosophy"],
      "Sayings and conversations of Confucius, gathered by his disciples: the founding text of Confucian ethics.",
      "The Analects is a collection of short exchanges between Confucius and his students, compiled after his "
      "death. It sketches the junzi, the exemplary person, who cultivates humaneness, keeps faith with others, "
      "honours ritual and never stops learning. Government should rule by virtue and example rather than "
      "punishment. Its brevity hides depth: for two thousand years, students across East Asia memorised it, and it "
      "shaped ideas of family, education and public service.",
      ["Ren (humaneness) is the heart of virtue: do not impose on others what you would not wish for yourself.",
       "Ritual and courtesy (li) shape character and hold society together.",
       "Rulers should lead by moral example; virtue spreads like wind over grass."],
      approx=True, original="論語 (Lúnyǔ)", pd=True, featured=True),
    W("dhammapada", "The Dhammapada", "the-buddha", -300, "scripture", "Pali", 100, 1,
      ["ethics", "philosophy-of-mind", "meaning-of-life"],
      "423 verses attributed to the Buddha on the mind, desire and the path to freedom from suffering.",
      "One of the best-loved texts of the Pali Canon, the Dhammapada gathers sayings attributed to the Buddha into "
      "26 chapters on themes such as the mind, the fool, the wise, anger and happiness. It opens with the claim "
      "that mind precedes all things: our thoughts shape our lives. Clear, rhythmic and practical, it has served "
      "for over two thousand years as a pocket guide to Buddhist ethics.",
      ["The mind shapes experience; train it, and happiness follows like a shadow.",
       "Hatred is never ended by hatred, only by non-hatred.",
       "Craving is the root of suffering; the wise loosen its hold through mindfulness."],
      approx=True, original="Dhammapada", pd=True),
    W("the-art-of-war", "The Art of War", "sun-tzu", -500, "treatise", "Classical Chinese", 100, 2,
      ["political-philosophy"],
      "Thirteen chapters of strategic wisdom: know yourself, know your enemy, and win without fighting if you can.",
      "The Art of War treats conflict as a matter of intelligence rather than brute force. Its thirteen chapters "
      "cover planning, terrain, manoeuvre, morale and the use of spies, always stressing preparation, adaptability "
      "and deception. The greatest victory is the one won without battle. Translated into French by a Jesuit "
      "missionary in 1772, it has since been read by generals, revolutionaries, athletes and executives as a "
      "philosophy of strategy.",
      ["Supreme excellence is to subdue the enemy without fighting.",
       "Know the enemy and know yourself, and you need not fear a hundred battles.",
       "All warfare is based on deception; be formless and adapt like water."],
      approx=True, original="孫子兵法 (Sūnzǐ bīngfǎ)", pd=True, featured=True),
    W("fragments-heraclitus", "Fragments", "heraclitus", -500, "aphorisms", "Ancient Greek", 60, 3,
      ["metaphysics", "epistemology"],
      "Around a hundred cryptic sayings on flux, fire, the logos and the hidden harmony of opposites.",
      "Heraclitus's book is lost; what remains are fragments quoted, often in order to disagree with them, by "
      "writers such as Plato, Aristotle and Hippolytus. They are short, oracular and endlessly suggestive: "
      "everything flows; the road up and the road down are one and the same; nature loves to hide. Read slowly, "
      "they reveal a coherent vision of a cosmos that is stable precisely because it is always changing.",
      ["Everything flows: the world is a process, not a collection of things.",
       "Opposites are unified; strife and tension sustain the order of the cosmos.",
       "A common logos governs all things, though most people live as if asleep to it."],
      approx=True, pd=True),
    W("on-nature-parmenides", "On Nature", "parmenides", -475, "poem", "Ancient Greek", 40, 4,
      ["metaphysics", "logic"],
      "A visionary poem in which a goddess proves that Being is one, eternal and unchanging.",
      "Parmenides' poem survives in about 160 lines. A young man is carried by chariot to a goddess who teaches him "
      "the 'Way of Truth': only what is can be thought or spoken of; nothing can come from nothing; so reality "
      "must be ungenerated, imperishable, whole and motionless. She then recounts the deceptive 'Way of Opinion' "
      "that mortals believe. Short but staggering, it set the agenda for Plato, Aristotle and all later "
      "metaphysics.",
      ["What is, is, and what is not cannot be thought.",
       "Coming-to-be and passing away are impossible, so change is illusion.",
       "Reason, not the senses, is the judge of reality."],
      approx=True, original="Περὶ φύσεως"),
    W("histories-herodotus", "The Histories", "herodotus", -430, "history", "Ancient Greek", 720, 3,
      ["history"],
      "The first great work of history: the epic story of the wars between Greece and Persia, and of the peoples "
      "caught up in them.",
      "Herodotus sets out to record 'great and marvellous deeds' so that they will not be forgotten, and to explain "
      "why Greeks and Persians fought. On the way he digresses gloriously into the customs of Egyptians, Scythians "
      "and Babylonians, the fortunes of Croesus and the rise of Cyrus, before building to Marathon, Thermopylae and "
      "Salamis. Gossipy, humane and wonderfully readable, the Histories also contain a quiet philosophy: fortune is "
      "unstable, and pride comes before a fall.",
      ["History is inquiry (historia): gather testimony, compare accounts, judge.",
       "Custom is king: every people thinks its own ways best.",
       "Human fortune is unstable; call no one happy until they are dead."],
      approx=True, original="Ἱστορίαι", pd=True, featured=True),
    W("apology", "Apology", "plato", -399, "dialogue", "Ancient Greek", 40, 1,
      ["ethics", "meaning-of-life", "epistemology"],
      "Socrates' defence speech at his trial for impiety—a portrait of the philosopher who would rather die than "
      "stop questioning.",
      "Plato's version of the speech Socrates gave before 501 Athenian jurors in 399 BCE. Socrates explains that "
      "the Delphic oracle called him the wisest of men, and that he could only make sense of this by realising "
      "that, unlike others, he did not think he knew what he did not know. Convicted, he refuses to stop "
      "philosophising or to propose exile, and faces death calmly. It is the best place to start reading Plato—and "
      "philosophy.",
      ["Wisdom begins with recognising the limits of one's own knowledge.",
       "The unexamined life is not worth living.",
       "A good person cannot truly be harmed; doing injustice is worse than suffering it."],
      approx=True, original="Ἀπολογία Σωκράτους", pd=True, featured=True),
    W("republic", "The Republic", "plato", -375, "dialogue", "Ancient Greek", 400, 3,
      ["political-philosophy", "ethics", "metaphysics", "epistemology"],
      "What is justice, and why be just? Plato answers by designing an ideal city ruled by philosopher-kings.",
      "The Republic begins with a simple question at a gathering in the port of Piraeus—what is justice?—and builds "
      "into the most ambitious work of ancient philosophy. Socrates constructs an ideal city to see justice 'writ "
      "large', with classes of rulers, guardians and producers mirroring reason, spirit and appetite in the soul. "
      "Along the way come the Ring of Gyges, the Allegory of the Cave, the theory of Forms, the critique of poetry "
      "and the Myth of Er. It remains a founding text of political thought, and a provocation.",
      ["Justice is a harmony in which each part of the soul or city does its proper work.",
       "The Allegory of the Cave: most people mistake shadows for reality; education turns the soul toward the "
       "light.",
       "Only philosophers, who love truth rather than power, should rule."],
      approx=True, original="Πολιτεία", pd=True, featured=True),
    W("symposium", "Symposium", "plato", -385, "dialogue", "Ancient Greek", 90, 2,
      ["aesthetics", "ethics", "meaning-of-life"],
      "At a drinking party in Athens, guests take turns praising Love—climaxing in Socrates' vision of the ascent "
      "to Beauty itself.",
      "Seven speakers, including the comic playwright Aristophanes and the tragedian Agathon, deliver speeches in "
      "praise of Eros. Aristophanes imagines humans as split halves searching for their other part; Socrates "
      "recounts the teaching of the priestess Diotima, who describes love as a ladder rising from one beautiful "
      "body to beautiful souls, laws and knowledge, and finally to Beauty itself. Then a drunken Alcibiades bursts "
      "in. It is perhaps Plato's most literary dialogue.",
      ["Love is desire for what we lack—ultimately for the good to be ours forever.",
       "The ladder of love leads from bodies to souls to the eternal Form of Beauty.",
       "Philosophy itself is a kind of erotic longing for wisdom."],
      approx=True, original="Συμπόσιον", pd=True),
    W("phaedo", "Phaedo", "plato", -380, "dialogue", "Ancient Greek", 90, 3,
      ["metaphysics", "philosophy-of-mind", "philosophy-of-religion"],
      "Socrates' last day: arguments for the immortality of the soul, and a death scene that has moved readers for "
      "millennia.",
      "Set in prison on the day of Socrates' execution, the Phaedo has him calmly arguing that philosophy is a "
      "preparation for death, since it frees the soul from the distractions of the body. He offers several "
      "arguments for the soul's immortality, develops the theory of Forms, and recounts a myth of the afterlife "
      "before drinking the hemlock. The closing pages are among the most famous in Greek literature.",
      ["Philosophy is the practice of dying: detaching the soul from bodily concerns.",
       "The soul, akin to the eternal Forms, outlasts the body.",
       "Learning may be recollection of knowledge the soul had before birth."],
      approx=True, original="Φαίδων", pd=True),
    W("meno", "Meno", "plato", -385, "dialogue", "Ancient Greek", 50, 2,
      ["epistemology", "ethics"],
      "Can virtue be taught? Socrates coaxes geometry out of an untutored boy to argue that learning is "
      "recollection.",
      "Meno arrives with a confident question—can virtue be taught?—and soon finds he cannot even define virtue. "
      "When he objects that you cannot search for what you do not know, Socrates questions an enslaved boy who, "
      "step by step, discovers how to double the area of a square. The dialogue's distinction between knowledge "
      "and true opinion, and its paradox of inquiry, still anchor discussions in epistemology.",
      ["Meno's paradox: how can we seek what we do not already know?",
       "Learning as recollection: the soul already holds knowledge waiting to be drawn out.",
       "Knowledge differs from true belief because it is 'tied down' by reasons."],
      approx=True, original="Μένων", pd=True),
    W("nicomachean-ethics", "Nicomachean Ethics", "aristotle", -340, "treatise", "Ancient Greek", 300, 3,
      ["ethics", "political-philosophy", "meaning-of-life"],
      "Aristotle's inquiry into the good life: happiness as flourishing, achieved through virtue, practical wisdom "
      "and friendship.",
      "Probably compiled from lecture notes and named after Aristotle's son Nicomachus, this is the founding text "
      "of virtue ethics. Everyone agrees the highest good is eudaimonia—happiness or flourishing—but what is it? "
      "Aristotle argues it is activity of the soul in accordance with virtue over a complete life. Virtues are "
      "stable dispositions, learned by habit, that hit the mean between extremes. Its books on friendship and on "
      "the contemplative life are among the richest in philosophy.",
      ["Eudaimonia, flourishing, is the highest human good.",
       "Virtue is a habit, a mean between excess and deficiency—courage lies between rashness and cowardice.",
       "Practical wisdom and true friendship are essential to a good life."],
      approx=True, original="Ἠθικὰ Νικομάχεια", pd=True, featured=True),
    W("politics-aristotle", "Politics", "aristotle", -330, "treatise", "Ancient Greek", 300, 3,
      ["political-philosophy", "society-and-economics"],
      "Humans are political animals: Aristotle studies constitutions, citizenship and the best possible state.",
      "Building on a survey of some 158 Greek constitutions collected by his school, Aristotle examines the "
      "household, slavery, property, citizenship and the merits of monarchy, aristocracy and democracy. The city "
      "exists by nature, he argues, for the sake of living well, not merely living. His favoured 'mixed' "
      "constitution, balancing rich and poor through a strong middle class, influenced republican thought from "
      "Polybius to the American founders—while his defence of natural slavery is a stark reminder of the limits of "
      "his age.",
      ["Humans are by nature political animals; we fulfil ourselves in community.",
       "Constitutions are good when they aim at the common good, corrupt when they serve the rulers alone.",
       "A large middle class makes a state stable."],
      approx=True, original="Πολιτικά", pd=True),
    W("metaphysics", "Metaphysics", "aristotle", -335, "treatise", "Ancient Greek", 400, 5,
      ["metaphysics"],
      "Aristotle's 'first philosophy': the study of being as being, substance, causes and the unmoved mover.",
      "The title, meaning 'after the Physics', was given by later editors, but the subject became a branch of "
      "philosophy. 'All men by nature desire to know', it begins. Aristotle surveys earlier thinkers, defends the "
      "principle of non-contradiction, analyses substance as the primary sense of being, distinguishes "
      "potentiality and actuality, and concludes with a divine unmoved mover—'thought thinking itself'. Dense and "
      "difficult, it shaped Islamic, Jewish and Christian theology.",
      ["Being is said in many ways, but primarily of substance.",
       "Everything that changes moves from potentiality to actuality.",
       "An eternal unmoved mover is the final cause of all motion."],
      approx=True, original="Τὰ μετὰ τὰ φυσικά"),
    W("poetics", "Poetics", "aristotle", -335, "treatise", "Ancient Greek", 60, 2,
      ["aesthetics"],
      "The first work of literary theory: what makes a tragedy work, from plot to catharsis.",
      "Responding in part to Plato's suspicion of poets, Aristotle argues that imitation (mimesis) is natural to "
      "humans and a source of learning. His analysis of tragedy—a unified plot with a beginning, middle and end; "
      "reversals and recognitions; a hero brought down by an error (hamartia); and the catharsis of pity and fear—"
      "has guided playwrights and screenwriters ever since. A second book, on comedy, is lost.",
      ["Art imitates life, and we learn through imitation.",
       "Plot is the soul of tragedy; character comes second.",
       "Tragedy arouses pity and fear to bring about their catharsis."],
      approx=True, original="Περὶ ποιητικῆς", pd=True),
    W("history-of-the-peloponnesian-war", "History of the Peloponnesian War", "thucydides", -400, "history",
      "Ancient Greek", 650, 4, ["history", "political-philosophy"],
      "A general's unflinching account of the war between Athens and Sparta—and of what power does to people.",
      "Thucydides began writing as soon as war broke out in 431 BCE, believing it would be the greatest conflict "
      "yet. His narrative, which breaks off in 411, is built from careful inquiry and set-piece speeches that "
      "dramatise the logic of each side. Pericles' Funeral Oration, the plague in Athens, the civil war at "
      "Corcyra, the Melian Dialogue and the disastrous Sicilian Expedition offer timeless lessons in fear, honour "
      "and interest.",
      ["Wars are driven by fear, honour and interest.",
       "In the Melian Dialogue, Athens claims that the strong do what they can and the weak suffer what they must.",
       "War is a violent teacher that degrades both language and morals."],
      approx=True, original="Ἱστορίαι", pd=True, featured=True),
    W("mencius", "Mencius", "mencius", -300, "book", "Classical Chinese", 200, 3,
      ["ethics", "political-philosophy"],
      "Dialogues with kings and disciples arguing that human nature is good and that government must serve the "
      "people.",
      "Compiled from Mencius's conversations, this book became one of the Four Books at the heart of Confucian "
      "education. Mencius argues that anyone who suddenly sees a child about to fall into a well feels alarm and "
      "compassion: such reactions prove we have innate moral 'sprouts'. Rulers should nurture the people "
      "materially and morally; those who become tyrants forfeit Heaven's mandate. Lively and argumentative, it shows "
      "Confucianism defending itself against rival schools.",
      ["Human nature is good; we have four innate sprouts of virtue.",
       "Moral growth requires cultivation, like tending crops—neither neglect nor forcing.",
       "The people are the most important element of a state; the ruler the least."],
      approx=True, original="孟子 (Mèngzǐ)", pd=True),
    W("zhuangzi", "Zhuangzi", "zhuangzi", -300, "book", "Classical Chinese", 300, 3,
      ["metaphysics", "epistemology", "meaning-of-life"],
      "Playful, profound parables of freedom: butterfly dreams, useless trees and the cook who carves by following "
      "the Way.",
      "The Zhuangzi—its 'inner chapters' probably by Zhuangzi himself, the rest by followers—is the second great "
      "classic of Taoism and one of the most delightful books in world philosophy. It mocks the certainties of "
      "Confucians and logicians, suggests that our perspectives are as limited as a frog's in a well, and praises "
      "the 'usefulness of the useless'. Cook Ding carves an ox effortlessly by following its natural structure; "
      "Zhuangzi drums and sings after his wife's death, seeing it as part of nature's transformations.",
      ["All perspectives are partial; wisdom loosens our grip on fixed distinctions.",
       "Skilful living means flowing with the natural grain of things.",
       "Death is a natural transformation, not something to dread."],
      approx=True, original="莊子 (Zhuāngzǐ)", pd=True),
    W("letter-to-menoeceus", "Letter to Menoeceus", "epicurus", -300, "letters", "Ancient Greek", 15, 1,
      ["ethics", "meaning-of-life"],
      "Epicurus' short summary of how to be happy: don't fear the gods or death, and seek pleasure wisely.",
      "Preserved by the biographer Diogenes Laërtius, this brief letter is the clearest statement of Epicurean "
      "ethics. It covers what later Epicureans summarised as the 'four-part cure': the gods are not to be feared, "
      "death is nothing to us, the good is easy to obtain, and the terrible is easy to endure. Pleasure is the goal "
      "of life—not the pleasures of the profligate, but the absence of bodily pain and mental disturbance, secured "
      "through prudence and simple living.",
      ["Death is nothing to us: where death is, we are not.",
       "Pleasure is the beginning and end of the blessed life—understood as tranquillity.",
       "Prudence is the greatest virtue; simple living brings the most security."],
      approx=True, original="Ἐπιστολὴ πρὸς Μενοικέα"),
    W("on-the-nature-of-things", "On the Nature of Things", "lucretius", -55, "poem", "Latin", 280, 3,
      ["metaphysics", "philosophy-of-science", "meaning-of-life"],
      "A six-book Latin poem explaining the universe through atoms and void—to free us from fear.",
      "Lucretius sets Epicurus's philosophy to verse of extraordinary beauty. Everything, he argues, is made of tiny "
      "indivisible atoms moving in an infinite void; their unpredictable 'swerve' makes free will possible; the "
      "soul is mortal; and the gods, if they exist, take no interest in us. The poem ranges over sensation, love, "
      "the origins of civilisation, thunder, magnets and plague. Its rediscovery in 1417 is sometimes credited with "
      "helping to spark the modern world.",
      ["Nothing comes from nothing; all things are atoms and void.",
       "The soul dies with the body, so death is not to be feared.",
       "Understanding nature frees us from superstition."],
      approx=True, original="De rerum natura", pd=True),
    W("on-duties", "On Duties", "cicero", -44, "treatise", "Latin", 200, 2,
      ["ethics", "political-philosophy"],
      "Cicero's last philosophical work, a letter to his son on honour, usefulness and public life.",
      "Written in the turbulent months after Caesar's assassination and addressed to his son Marcus, then a student "
      "in Athens, On Duties draws on the Stoic Panaetius to explain what is honourable, what is useful, and what to "
      "do when they seem to conflict—Cicero's answer being that they never truly do. Among the first classical "
      "texts ever printed, its ideals of justice, good faith and public service shaped European education for "
      "centuries.",
      ["Nothing truly useful can be dishonourable.",
       "Justice and good faith are the foundations of society.",
       "We are not born for ourselves alone; our country and friends have claims on us."],
      original="De officiis", pd=True),
    W("letters-from-a-stoic", "Letters from a Stoic", "seneca", 65, "letters", "Latin", 250, 2,
      ["ethics", "meaning-of-life"],
      "Seneca's letters of friendly, practical Stoic advice on time, fear, friendship, wealth and death.",
      "In the last years of his life Seneca wrote 124 letters to his friend Lucilius, then a Roman official in "
      "Sicily. Each takes up an everyday matter—crowds, travel, noise, illness, slavery, old age—and turns it into "
      "a lesson in living well. Warm, quotable and surprisingly modern, they show philosophy as a daily practice of "
      "self-examination. Seneca freely borrows from Epicurus too: whatever is well said by anyone, he says, belongs "
      "to him.",
      ["Time is our only true possession; guard it carefully.",
       "We suffer more often in imagination than in reality.",
       "Treat slaves as fellow human beings—'they are slaves, but they are also men'."],
      approx=True, original="Epistulae morales ad Lucilium", pd=True, featured=True),
    W("on-the-shortness-of-life", "On the Shortness of Life", "seneca", 49, "essay", "Latin", 40, 1,
      ["meaning-of-life", "ethics"],
      "Life is long enough—if you know how to use it. Seneca's essay against busyness.",
      "Addressed to Paulinus, who managed Rome's grain supply, this short essay argues that we complain life is "
      "short while squandering it on ambition, luxury, vanity and other people's demands. The truly alive are those "
      "who make time for philosophy, conversing with the great minds of the past. Two thousand years before the "
      "smartphone, it remains a bracing diagnosis of distraction.",
      ["Life is not short; we make it short by wasting it.",
       "The busy are the least able to truly live.",
       "Studying the wise of the past adds their ages to our own."],
      approx=True, original="De brevitate vitae", pd=True),
    W("parallel-lives", "Parallel Lives", "plutarch", 100, "history", "Ancient Greek", 1300, 3,
      ["history", "ethics"],
      "Paired biographies of famous Greeks and Romans, written to reveal character through deeds great and small.",
      "Plutarch pairs, for example, Alexander with Caesar and Demosthenes with Cicero, often following each pair "
      "with a comparison. He insists he is writing lives, not histories: a casual remark or a jest can reveal more "
      "about character than battles where thousands fall. Translated into English by Thomas North in 1579, the "
      "Lives supplied Shakespeare with plots and generations of readers with models of virtue and vice.",
      ["Character, not events alone, explains history.",
       "Small gestures reveal more than great deeds.",
       "Examples of the great can train our own moral judgement."],
      approx=True, original="Βίοι Παράλληλοι", pd=True),
    W("enchiridion", "Enchiridion", "epictetus", 125, "book", "Ancient Greek", 30, 1,
      ["ethics", "meaning-of-life"],
      "The Stoic 'handbook': a pocket-sized guide to telling apart what is up to you and what is not.",
      "Compiled by Epictetus's student Arrian as a digest of his master's teaching, the Enchiridion ('handbook') is "
      "short enough to read in an hour and deep enough to live by for a lifetime. It opens with the Stoic "
      "dichotomy of control: our judgements, desires and actions are up to us; our bodies, reputation and fortune "
      "are not. Disturbance comes from wanting the second to behave like the first.",
      ["Some things are up to us, others are not; focus only on the first.",
       "We are disturbed not by things but by our judgements about them.",
       "Play well the role you are given; choosing the role belongs to another."],
      approx=True, original="Ἐγχειρίδιον", pd=True, featured=True),
    W("discourses-epictetus", "Discourses", "epictetus", 108, "lectures", "Ancient Greek", 400, 2,
      ["ethics", "meaning-of-life"],
      "Lively, blunt lectures from Epictetus' school, recorded by his student Arrian.",
      "Four books survive of the Discourses, Arrian's record of Epictetus' informal talks with students at "
      "Nicopolis. Fuller and funnier than the Enchiridion, they show a teacher who mocks pretension, drills "
      "students in handling insults, exile and loss, and insists that philosophy is useless unless practised. Their "
      "influence runs from Marcus Aurelius to modern cognitive therapy.",
      ["Freedom is wanting only what is in your power.",
       "Philosophy is training, not talk.",
       "Every situation has two handles; take it by the one you can carry."],
      approx=True, original="Διατριβαί", pd=True),
    W("meditations", "Meditations", "marcus-aurelius", 175, "book", "Ancient Greek", 250, 1,
      ["ethics", "meaning-of-life"],
      "The private journal of a Roman emperor, reminding himself how to be good, calm and unafraid of death.",
      "Marcus Aurelius never intended these twelve books of notes for anyone but himself; their Greek title means "
      "simply 'to himself'. Written largely during military campaigns, they return again and again to a few Stoic "
      "themes: live according to nature and reason, accept what fate brings, serve the common good, and remember "
      "how brief and small human life is. The result is one of the most honest and consoling books ever written.",
      ["What stands in the way becomes the way: obstacles are material for virtue.",
       "Everything changes and life is brief, so act well now.",
       "We are made for cooperation, like hands and feet; serve the common good."],
      approx=True, original="Τὰ εἰς ἑαυτόν", pd=True, featured=True),
    W("fundamental-verses-on-the-middle-way", "The Fundamental Verses on the Middle Way", "nagarjuna", 200,
      "treatise", "Sanskrit", 120, 5, ["metaphysics", "logic", "epistemology"],
      "Nagarjuna's masterpiece: rigorous verses showing that nothing exists independently—everything is 'empty'.",
      "In 27 chapters of terse verses, Nagarjuna examines causation, motion, the self, time, the Buddha and nirvana "
      "itself, showing that each, examined closely, cannot have intrinsic, independent existence. Things arise only "
      "in dependence on other things—and that dependent arising is what 'emptiness' means. This is not nihilism but "
      "a middle way between eternalism and annihilation. Its distinction between conventional and ultimate truth "
      "became central to Mahayana Buddhism.",
      ["Whatever arises dependently is empty of intrinsic existence.",
       "Emptiness is itself empty: it is not a hidden absolute.",
       "There are two truths, conventional and ultimate; liberation requires understanding both."],
      approx=True, original="Mūlamadhyamakakārikā"),
    W("outlines-of-pyrrhonism", "Outlines of Pyrrhonism", "sextus-empiricus", 200, "treatise", "Ancient Greek",
      250, 4, ["epistemology", "logic"],
      "The handbook of ancient skepticism: how to suspend judgement—and find peace in doing so.",
      "Sextus explains that the skeptic is not someone who denies knowledge but someone who keeps inquiring. For "
      "any claim, an opposing claim of equal force can be found, using standard 'modes' that exploit differences "
      "between animals, people, senses, circumstances and cultures. Faced with this balance, the skeptic suspends "
      "judgement and finds—like the painter who threw his sponge at a picture in frustration and accidentally "
      "produced the effect he wanted—that tranquillity follows.",
      ["For every argument an equal and opposite argument can be found.",
       "Suspension of judgement (epoché) brings tranquillity (ataraxia).",
       "The skeptic lives by appearances and custom, without dogmatic belief."],
      approx=True, original="Πυρρώνειοι ὑποτυπώσεις"),
    W("enneads", "The Enneads", "plotinus", 270, "treatise", "Ancient Greek", 600, 5,
      ["metaphysics", "philosophy-of-religion"],
      "Plotinus' treatises, arranged by Porphyry in six sets of nine, describing the ascent of the soul to the One.",
      "Plotinus wrote his treatises late in life, in response to discussions in his seminar; his student Porphyry "
      "later edited them into six groups of nine ('enneads'). They describe a hierarchy of reality emanating from "
      "the One, which is beyond being and thought, through Intellect, home of the Forms, to Soul, which animates the "
      "cosmos. The human task is to turn inward and upward, purifying the soul until it is united with its source—"
      "'the flight of the alone to the alone'.",
      ["All reality flows from a single, ineffable source: the One.",
       "The soul belongs to a higher world and can return to it through contemplation.",
       "Beauty in the world is a trace of the intelligible order."],
      approx=True, original="Ἐννεάδες"),
    W("confessions", "Confessions", "augustine", 400, "book", "Latin", 350, 3,
      ["philosophy-of-religion", "philosophy-of-mind", "meaning-of-life"],
      "The first great autobiography: Augustine's restless journey from ambition and desire to faith.",
      "Written as a long prayer addressed to God, the Confessions recounts Augustine's childhood theft of pears, "
      "his student years in Carthage, his search through Manichaeism and Neoplatonism, his long relationship with "
      "an unnamed partner, his devout mother Monica, and his conversion in a Milan garden. The final books turn to "
      "philosophy: memory, creation and the nature of time ('If no one asks me, I know; if I wish to explain it, "
      "I do not know'). Its inwardness changed literature.",
      ["Our heart is restless until it rests in God.",
       "Time exists in the mind, as memory, attention and expectation.",
       "The will is divided against itself; we often fail to do the good we want."],
      approx=True, original="Confessiones", pd=True, featured=True),
    W("city-of-god", "The City of God", "augustine", 426, "book", "Latin", 1100, 4,
      ["philosophy-of-religion", "history", "political-philosophy"],
      "Written after the sack of Rome, Augustine's vast vision of history as a tale of two cities.",
      "When the Visigoths sacked Rome in 410, pagans blamed the abandonment of the old gods. Augustine's reply, "
      "written over thirteen years, grew into a philosophy of history. Humanity is divided into two 'cities' "
      "defined by their loves: the earthly city, built on love of self, and the city of God, built on love of God. "
      "No earthly empire, not even a Christian Rome, is the kingdom of God. Its ideas on war, peace and the limits "
      "of politics shaped medieval Europe.",
      ["Two loves have made two cities: love of self and love of God.",
       "Earthly peace is valuable but provisional; no state is ultimate.",
       "History has a direction and a meaning beyond the rise and fall of empires."],
      original="De civitate Dei", pd=True),

    # ── Middle Ages ────────────────────────────────────────────────────────
    W("consolation-of-philosophy", "The Consolation of Philosophy", "boethius", 524, "book", "Latin", 160, 2,
      ["meaning-of-life", "philosophy-of-religion", "ethics"],
      "Awaiting execution, Boethius is visited by Lady Philosophy, who teaches him what true happiness is.",
      "Alternating prose and verse, Boethius imagines himself in prison, bitterly lamenting his fall, when a "
      "majestic woman—Philosophy herself—appears at his bedside. She diagnoses his illness and treats it: Fortune's "
      "wheel always turns, so wealth, power and fame were never truly his; real happiness is the highest good, "
      "which is God; and divine foreknowledge does not destroy human freedom. King Alfred, Chaucer and Elizabeth I "
      "all translated it.",
      ["Fortune is fickle by nature; do not stake happiness on her gifts.",
       "True happiness is the highest good, which cannot be taken away.",
       "God's eternal knowledge does not compel our free choices."],
      approx=True, original="De consolatione philosophiae", pd=True, featured=True),
    W("the-virtuous-city", "The Virtuous City", "al-farabi", 943, "treatise", "Arabic", 150, 4,
      ["political-philosophy", "metaphysics"],
      "Al-Farabi's vision of a perfect society led by a philosopher-prophet, built on a Neoplatonic cosmos.",
      "Its full title is The Principles of the Opinions of the Inhabitants of the Virtuous City. The book begins "
      "with the First Cause and the emanation of the heavens and only then turns to human society—because, for "
      "al-Farabi, the good city must mirror the order of the cosmos. Its ruler unites philosophical wisdom with "
      "prophetic imagination, and its citizens cooperate toward true happiness. He then catalogues 'ignorant', "
      "'wicked' and 'erring' cities that pursue wealth, honour or pleasure instead.",
      ["Human happiness is achieved in community, not alone.",
       "The ideal ruler combines philosophy with the gift of prophecy and persuasion.",
       "Cities fail when they pursue wealth, honour or pleasure instead of true happiness."],
      approx=True, original="Mabādiʾ ārāʾ ahl al-madīna al-fāḍila"),
    W("the-book-of-healing", "The Book of Healing", "avicenna", 1027, "treatise", "Arabic", 1500, 5,
      ["metaphysics", "logic", "philosophy-of-mind", "philosophy-of-science"],
      "Avicenna's vast encyclopedia of philosophy and science—a cure for the soul's ignorance.",
      "Despite its title, the Shifa is not a medical work: it 'heals' the soul of error. Covering logic, the "
      "natural sciences, mathematics and metaphysics, it reworks Aristotle into an original system. Here Avicenna "
      "presents the distinction between essence and existence, the proof of a Necessary Existent whose essence is "
      "to exist, and the 'floating man'—a person created in mid-air without any sensation who would still know "
      "that he exists. Latin translations made it a major source for scholasticism.",
      ["Essence and existence are distinct in all things except God.",
       "A Necessary Existent must ground the chain of contingent beings.",
       "The 'floating man': self-awareness does not depend on the body."],
      approx=True, original="Kitāb al-Shifāʾ"),
    W("proslogion", "Proslogion", "anselm", 1078, "treatise", "Latin", 40, 3,
      ["philosophy-of-religion", "metaphysics"],
      "A short meditation containing the famous 'ontological argument' that God must exist.",
      "Written as a prayerful address to God by a monk seeking to understand what he believes, the Proslogion "
      "looks for a single argument for God's existence. God is 'that than which nothing greater can be conceived'. "
      "Even the fool who denies God understands this idea; but a being that existed only in the understanding "
      "would be less great than one that existed in reality too. A monk named Gaunilo replied with the idea of a "
      "perfect island, launching a debate that Descartes, Kant and modern logicians have continued.",
      ["God is that than which nothing greater can be conceived.",
       "To exist in reality is greater than to exist only in thought.",
       "Faith seeks understanding: reason deepens what belief already holds."],
      approx=True, pd=True),
    W("incoherence-of-the-philosophers", "The Incoherence of the Philosophers", "al-ghazali", 1095, "treatise",
      "Arabic", 250, 4, ["philosophy-of-religion", "metaphysics", "epistemology"],
      "Al-Ghazali turns the philosophers' own logic against them in twenty disputed questions.",
      "Al-Ghazali studied the philosophers—above all Avicenna—so thoroughly that he could summarise their views "
      "better than many followers, then set out to show that their metaphysical claims were not demonstrated. He "
      "targets twenty theses and condemns three as unbelief: the eternity of the world, God's knowing only "
      "universals, and the denial of bodily resurrection. Most famously, he argues that fire burning cotton is not "
      "a necessary connection but a regularity God creates—an analysis of causation often compared to Hume's.",
      ["The philosophers' metaphysics falls short of the rigorous proof they claim.",
       "Causal necessity is never observed; events follow one another by God's custom.",
       "The world was created in time by divine will, not eternal."],
      original="Tahāfut al-falāsifa"),
    W("deliverance-from-error", "Deliverance from Error", "al-ghazali", 1108, "book", "Arabic", 80, 2,
      ["epistemology", "philosophy-of-religion", "meaning-of-life"],
      "Al-Ghazali's intellectual autobiography: radical doubt, spiritual crisis and the path of the Sufis.",
      "Late in life, al-Ghazali told the story of his search for certainty. Doubting the senses and even reason, he "
      "fell into a skepticism from which, he says, he was freed only by a light God cast into his heart. He then "
      "examined theologians, philosophers and esoteric sectarians before finding in Sufism a knowledge that is "
      "tasted, not merely learned. Its method of doubt is often compared to Descartes' half a millennium later.",
      ["Certainty must withstand every possible doubt.",
       "The senses and reason can both deceive.",
       "The highest knowledge is experiential 'tasting' (dhawq), not argument alone."],
      approx=True, original="al-Munqidh min al-ḍalāl"),
    W("incoherence-of-the-incoherence", "The Incoherence of the Incoherence", "averroes", 1180, "treatise",
      "Arabic", 400, 5, ["philosophy-of-religion", "metaphysics"],
      "Averroes' point-by-point reply to al-Ghazali, defending reason and philosophy.",
      "Averroes quotes al-Ghazali's Incoherence passage by passage and responds, sometimes defending Avicenna, "
      "sometimes conceding that Avicenna erred, and always insisting on the integrity of demonstrative reasoning. "
      "To deny real causes in things, he argues, is to destroy knowledge itself. Its companion work, the Decisive "
      "Treatise, argues that Islamic law commands philosophical study for those capable of it.",
      ["Denying natural causation destroys the possibility of knowledge.",
       "Truth does not contradict truth: sound philosophy and revelation agree.",
       "People reach truth in different ways—by demonstration, dialectic or rhetoric."],
      approx=True, original="Tahāfut al-tahāfut"),
    W("guide-for-the-perplexed", "The Guide for the Perplexed", "maimonides", 1190, "treatise", "Judeo-Arabic",
      650, 4, ["philosophy-of-religion", "metaphysics", "ethics"],
      "Written for a student torn between faith and philosophy, Maimonides' masterpiece reads scripture through "
      "reason.",
      "Maimonides wrote the Guide as a long letter to a gifted student perplexed by the apparent conflict between "
      "the Torah's language and Aristotelian philosophy. He argues that biblical descriptions of God's body and "
      "emotions are metaphors, that God can be described only by negation, and weighs the arguments for and "
      "against the eternity of the world. Written in a deliberately guarded style, it was banned and burned by some "
      "and revered by others, and influenced Aquinas and Spinoza.",
      ["Scripture's descriptions of God's body and emotions are metaphors.",
       "We can say only what God is not (negative theology).",
       "Reason and revelation, rightly understood, do not conflict."],
      approx=True, original="Dalālat al-ḥāʾirīn", pd=True),
    W("summa-theologica", "Summa Theologica", "thomas-aquinas", 1270, "treatise", "Latin", 3000, 5,
      ["philosophy-of-religion", "ethics", "metaphysics", "political-philosophy"],
      "Aquinas' unfinished masterwork: a systematic map of theology, ethics and human nature, question by question.",
      "Intended as a textbook for beginners, the Summa runs to thousands of articles. Each poses a question, lists "
      "objections, cites an authority 'on the contrary', gives Aquinas' answer and replies to every objection—a "
      "model of fair disputation. It contains the Five Ways for God's existence, treatises on human acts, virtues, "
      "law and natural law, and a theology of creation and grace. Aquinas stopped writing in December 1273 and died "
      "a few months later; it remains a pillar of Catholic thought.",
      ["Five Ways: God's existence can be shown from motion, causation, contingency, gradation and order.",
       "Natural law is human reason's participation in the eternal law.",
       "Grace does not destroy nature but perfects it."],
      approx=True, original="Summa Theologiae", pd=True),
    W("summa-logicae", "Summa Logicae", "william-of-ockham", 1323, "treatise", "Latin", 400, 5,
      ["logic", "philosophy-of-language", "metaphysics"],
      "Ockham's comprehensive logic textbook and the foundation of his nominalism.",
      "Ockham's 'Sum of Logic' covers terms, propositions and arguments, but at its heart is a theory of "
      "signification in which only individuals exist and general terms are mental signs standing for many "
      "individuals. Universals are not things in the world. Combined with his principle of parsimony—plurality "
      "should not be posited without necessity—this cut away much of the ontology of earlier scholastics and paved "
      "the way for modern empiricism.",
      ["Only individuals exist; universals are concepts or names.",
       "Do not multiply entities beyond necessity (Ockham's razor).",
       "Logic studies how mental, spoken and written signs stand for things."],
      approx=True),
    W("shobogenzo", "Shōbōgenzō", "dogen", 1253, "essay", "Japanese", 1000, 5,
      ["metaphysics", "meaning-of-life"],
      "Dōgen's collection of Zen essays on practice, time, being and enlightenment.",
      "The 'Treasury of the True Dharma Eye' is a collection of essays Dōgen wrote over two decades, unusually in "
      "Japanese rather than classical Chinese. Dense, poetic and full of wordplay, it argues that practice and "
      "enlightenment are one, that all beings are Buddha-nature, and—in the essay 'Uji' ('Being-Time')—that time "
      "is not a container for things but existence itself. Long read mainly within Sōtō Zen, it is now studied by "
      "philosophers worldwide.",
      ["Practice and enlightenment are one; sitting meditation expresses awakening rather than leading to it.",
       "Being is time: each moment is the whole of existence.",
       "To study the self is to forget the self."],
      approx=True, original="正法眼蔵"),
    W("muqaddimah", "The Muqaddimah", "ibn-khaldun", 1377, "history", "Arabic", 500, 3,
      ["history", "society-and-economics", "political-philosophy"],
      "Ibn Khaldun's 'Introduction' to history: a theory of how civilisations rise and fall.",
      "Written as the introduction to a universal history, the Muqaddimah criticises historians who uncritically "
      "repeat impossible reports and proposes a new 'science of civilisation'. Its central concept is asabiyya—"
      "group cohesion—which lets hardy nomadic peoples conquer cities and found dynasties that, softened by "
      "luxury, decline within a few generations. It also offers penetrating analyses of labour, taxation, "
      "education and urban life, centuries before Montesquieu and Adam Smith.",
      ["Group solidarity (asabiyya) drives the rise of dynasties; its loss brings decline.",
       "Dynasties typically last only three or four generations.",
       "Historians must test reports against what is possible in human society."],
      original="al-Muqaddimah", featured=True),

    # ── Renaissance ────────────────────────────────────────────────────────
    W("in-praise-of-folly", "In Praise of Folly", "erasmus", 1511, "essay", "Latin", 150, 2,
      ["ethics", "philosophy-of-religion"],
      "Folly herself delivers a speech in her own praise—a satire on theologians, monks, princes and the rest of us.",
      "Conceived while Erasmus was travelling to England to stay with Thomas More (the Latin title puns on his "
      "name), In Praise of Folly has Folly, a goddess, boasting that without her no one would marry, have children "
      "or enjoy life. Gradually the satire sharpens against scholastic theologians, corrupt clergy and warmongering "
      "popes—and then turns again to praise the holy 'folly' of Christian love. Its mixture of laughter and reform "
      "made it a bestseller of the age of printing.",
      ["Some foolishness—illusion, self-love, play—makes life bearable.",
       "Pride and pedantry among the learned and powerful are the real folly.",
       "The deepest wisdom may look like folly to the world."],
      original="Moriae encomium", pd=True),
    W("the-prince", "The Prince", "machiavelli", 1532, "treatise", "Italian", 120, 2,
      ["political-philosophy"],
      "A short, shocking handbook on how to win and keep power—as rulers actually do, not as they should.",
      "Written in 1513 after the Medici returned to Florence and Machiavelli lost his post, The Prince was "
      "dedicated to a Medici prince in hopes of employment, and published only in 1532, after its author's death. "
      "Drawing on ancient and recent examples—especially Cesare Borgia—Machiavelli advises that a prince must be "
      "willing to be cruel, deceptive and feared when necessary, and must master fortune through virtù. It was "
      "placed on the Church's Index of forbidden books and has never stopped provoking readers.",
      ["If you cannot be both, it is safer to be feared than loved.",
       "A ruler must learn how not to be good, and use this according to necessity.",
       "Virtù—bold skill—can master half of fortune."],
      original="Il Principe", pd=True, featured=True),
    W("utopia", "Utopia", "thomas-more", 1516, "book", "Latin", 130, 2,
      ["political-philosophy", "society-and-economics"],
      "A traveller describes an island where property is shared, gold is scorned and religion is tolerated.",
      "Book One is a sharp debate about England, where enclosures are turning farmland into sheep pasture and "
      "thieves are hanged for stealing bread—sheep, says one speaker, now 'devour men'. In Book Two, the traveller "
      "Raphael Hythloday describes Utopia, an island with no private property, six-hour workdays, elected officials "
      "and religious toleration—but also slavery and strict control. More never says whether he means it as "
      "blueprint, satire or thought experiment, and the genre it named has been arguing ever since.",
      ["Private property and greed lie at the root of social evils.",
       "Punishment without addressing poverty is both cruel and useless.",
       "A good society may need radically different institutions from our own."],
      original="Utopia", pd=True),
    W("instructions-for-practical-living", "Instructions for Practical Living", "wang-yangming", 1518, "book",
      "Classical Chinese", 300, 3, ["ethics", "epistemology"],
      "Wang Yangming's recorded conversations on innate moral knowing and the unity of knowledge and action.",
      "Compiled by his students, the Chuanxi lu presents Wang Yangming's rebellion against the orthodox "
      "Neo-Confucian method of investigating external things. Moral principles, he says, are not out there to be "
      "found but in the mind; everyone has innate knowledge of the good, which must be extended through practice. "
      "Knowing and acting are one: someone who claims to know filial piety but does not practise it does not "
      "really know it.",
      ["The mind is principle; moral truth is found within.",
       "Everyone possesses innate knowledge of the good (liangzhi).",
       "Knowledge and action form a unity; to truly know is to act."],
      approx=True, original="傳習錄 (Chuánxí lù)"),
    W("essays-montaigne", "Essays", "montaigne", 1580, "essay", "French", 1100, 2,
      ["ethics", "epistemology", "meaning-of-life"],
      "Montaigne invents the essay, testing his judgement on everything—and finding all of humanity in himself.",
      "Montaigne's three books of Essays (1580–1588) take up subjects as varied as sadness, smells, thumbs, "
      "cannibals, coaches and experience. Wandering, digressive and frank, they are a portrait of a mind in motion: "
      "'I do not portray being: I portray passing.' Behind the charm lies a serious skepticism about human reason, "
      "a hatred of cruelty, and a humane acceptance of our mixed, mortal condition. Every essayist since has been "
      "in his debt.",
      ["'What do I know?': humility about the limits of human reason.",
       "Each person bears the entire form of the human condition.",
       "To philosophise is to learn how to die—and how to live well."],
      original="Essais", pd=True, featured=True),
    W("novum-organum", "Novum Organum", "francis-bacon", 1620, "treatise", "Latin", 300, 3,
      ["philosophy-of-science", "epistemology"],
      "Bacon's 'new instrument' for science: careful induction instead of deduction from authority.",
      "Meant to replace Aristotle's logical works (the Organon), Bacon's book argues that human understanding is "
      "distorted by 'idols': of the tribe (human nature), the cave (individual bias), the marketplace (language) "
      "and the theatre (philosophical systems). Science should proceed by systematic observation and experiment, "
      "building cautiously from particular facts to general laws and seeking out negative instances. It inspired "
      "the founders of the Royal Society.",
      ["Four 'idols' distort human understanding.",
       "True knowledge comes from patient induction, not deduction from authority.",
       "Knowledge exists to improve human life."],
      original="Novum Organum Scientiarum", pd=True),
]
