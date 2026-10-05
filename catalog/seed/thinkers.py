"""Thinkers in the catalogue. Years are signed (negative = BCE)."""


def T(slug, name, born, died, place, era, schools, topics, influences, tagline, bio, approx=False, dates=""):
    return dict(
        slug=slug, name=name, born=born, died=died, place=place, era=era, schools=schools, topics=topics,
        influences=influences, tagline=tagline, bio=bio, approx=approx, dates=dates,
    )


THINKERS = [
    # ── Antiquity ──────────────────────────────────────────────────────────
    T("laozi", "Laozi", -571, None, "State of Chu, China", "ancient", ["taoism"],
      ["metaphysics", "ethics", "political-philosophy"], [],
      "Legendary sage credited with the Tao Te Ching and the founding of Taoism.",
      "Laozi ('Old Master') is the traditional author of the Tao Te Ching, though historians debate whether he was "
      "a single person, a composite or a legend. Tradition makes him an archivist at the Zhou court and an older "
      "contemporary of Confucius who, disillusioned with the dynasty's decline, rode west and left his teachings "
      "with a border guard. Whatever his historicity, the text attributed to him became one of the most translated "
      "books on Earth, shaping Chinese religion, art, government and medicine, and offering a vision of wisdom "
      "built on simplicity, humility and effortless action (wu wei).",
      approx=True, dates="fl. 6th century BCE (traditional)"),
    T("confucius", "Confucius", -551, -479, "Qufu, State of Lu, China", "ancient", ["confucianism"],
      ["ethics", "political-philosophy"], [],
      "Chinese teacher whose ethics of virtue, ritual and learning shaped East Asia for two millennia.",
      "Kong Fuzi, latinised as Confucius, was a minor official and itinerant teacher in the troubled Spring and "
      "Autumn period. He never found a ruler willing to put his ideas into practice, but his students preserved "
      "his conversations in the Analects. Confucius taught that a good society grows from good people: cultivate "
      "humaneness (ren), honour ritual propriety (li), love learning, and fulfil the duties of your relationships. "
      "Adopted as state orthodoxy under the Han dynasty, his teaching became the backbone of education and "
      "government across China, Korea, Japan and Vietnam."),
    T("the-buddha", "Siddhartha Gautama (the Buddha)", -563, -483, "Lumbini (present-day Nepal)", "ancient",
      ["buddhism"], ["ethics", "metaphysics", "philosophy-of-mind", "meaning-of-life"], [],
      "Indian teacher whose path to the end of suffering became Buddhism.",
      "Born a prince of the Shakya clan in the foothills of the Himalayas, Siddhartha Gautama is said to have "
      "abandoned a sheltered life after encountering old age, sickness and death. After years of ascetic practice "
      "he sought a 'middle way' and, according to tradition, attained awakening while meditating beneath a tree at "
      "Bodh Gaya. For some four decades he taught across northern India: that suffering arises from craving, that "
      "it can cease, and that an eightfold path of ethics, meditation and wisdom leads there. His analysis of the "
      "self as a changing process anticipates debates in modern philosophy of mind.",
      approx=True, dates="c. 5th century BCE"),
    T("heraclitus", "Heraclitus", -535, -475, "Ephesus, Ionia", "ancient", ["presocratics"],
      ["metaphysics", "epistemology"], [],
      "The 'obscure' philosopher of flux, fire and the unity of opposites.",
      "An aristocrat of Ephesus who reportedly refused political office, Heraclitus wrote a single book that "
      "survives only in about a hundred cryptic fragments quoted by later authors. He taught that the world is in "
      "ceaseless change, governed by a rational principle he called the logos, and that opposites—day and night, "
      "war and peace—are bound together in tension. His oracular style earned him the nickname 'the Obscure', but "
      "his ideas echo through Plato, the Stoics, Hegel and Nietzsche.",
      approx=True),
    T("parmenides", "Parmenides", -515, -450, "Elea, Magna Graecia", "ancient", ["presocratics"],
      ["metaphysics", "logic"], [],
      "Founder of the Eleatic school, who argued that change is an illusion.",
      "Parmenides of Elea wrote a philosophical poem in which a goddess reveals two paths: the 'Way of Truth' and "
      "the 'Way of Opinion'. Reasoning purely from the premise that 'what is, is' and that 'what is not' cannot be "
      "thought, he concluded that reality must be one, unchanging and indivisible—so the change and plurality we "
      "perceive are illusions. It was perhaps the first sustained deductive argument in Western thought. Plato "
      "called him 'venerable and awesome', and every later metaphysics had to answer him.",
      approx=True),
    T("sun-tzu", "Sun Tzu", -544, -496, "State of Qi, China", "ancient", ["political-realism"],
      ["political-philosophy"], [],
      "Chinese general and strategist, traditional author of The Art of War.",
      "According to the historian Sima Qian, Sun Wu—honoured as Sun Tzu, 'Master Sun'—was a general who served "
      "King Helü of Wu around the end of the sixth century BCE. Modern scholars think The Art of War was probably "
      "compiled somewhat later, perhaps by his followers, but the work bearing his name became the most influential "
      "military treatise in history. Its insistence on knowledge, deception, flexibility and winning without "
      "fighting has been studied by generals, emperors, diplomats and, more recently, business leaders.",
      approx=True, dates="fl. late 6th century BCE (traditional)"),
    T("herodotus", "Herodotus", -484, -425, "Halicarnassus, Caria", "ancient", ["historiography"],
      ["history"], [],
      "The 'Father of History', chronicler of the wars between Greece and Persia.",
      "Born in Halicarnassus on the coast of Asia Minor, then under Persian rule, Herodotus travelled widely "
      "through the Greek world, Egypt and the Near East collecting stories. His Histories set out to preserve "
      "'great and marvellous deeds' and to explain why Greeks and Persians went to war. Cicero called him the "
      "Father of History; critics called him the Father of Lies for his credulous tales. Both labels contain "
      "truth: his curiosity about foreign customs and his habit of weighing competing accounts founded history and "
      "ethnography as disciplines.",
      approx=True),
    T("socrates", "Socrates", -470, -399, "Athens", "ancient", [],
      ["ethics", "epistemology"], [],
      "The Athenian questioner who made philosophy a way of life—and died for it.",
      "Socrates wrote nothing. We know him through the dialogues of his student Plato, the memoirs of Xenophon and "
      "a mocking caricature in Aristophanes' Clouds. A stonemason's son who served bravely as a hoplite, he spent "
      "his days in the Athenian marketplace cross-examining anyone who claimed to know what justice, courage or "
      "piety are—usually showing that they did not. Professing that his only wisdom was knowing that he did not "
      "know, he insisted that caring for one's soul mattered more than wealth or reputation. In 399 BCE Athens "
      "convicted him of impiety and corrupting the youth, and he drank hemlock rather than abandon his calling.",
      approx=True, dates="c. 470 – 399 BCE"),
    T("plato", "Plato", -428, -348, "Athens", "ancient", ["platonism"],
      ["metaphysics", "ethics", "political-philosophy", "epistemology", "aesthetics"],
      ["socrates", "parmenides", "heraclitus"],
      "Socrates' student, founder of the Academy, and author of the dialogues that launched Western philosophy.",
      "Born into a prominent Athenian family, Plato was shaped by the execution of his teacher Socrates. He "
      "travelled, then founded the Academy around 387 BCE—arguably the first university—which endured for "
      "centuries. His dialogues, almost all starring Socrates, range across justice, love, knowledge, death and the "
      "soul. Their most famous doctrine holds that the changing world of the senses is a shadow of eternal Forms "
      "grasped by reason. Alfred North Whitehead quipped that the European philosophical tradition is 'a series of "
      "footnotes to Plato'.",
      approx=True),
    T("thucydides", "Thucydides", -460, -400, "Athens", "ancient", ["historiography", "political-realism"],
      ["history", "political-philosophy"], ["herodotus"],
      "Athenian general who wrote the first critical history of war and power.",
      "An Athenian general exiled after failing to save the city of Amphipolis in 424 BCE, Thucydides spent the "
      "rest of the Peloponnesian War observing both sides. His History rejects myth and divine intervention, seeks "
      "accurate evidence, and explains events by human nature, fear and interest. He meant it to be 'a possession "
      "for all time', and it has been: statesmen and theorists of international relations still debate the Melian "
      "Dialogue and the so-called 'Thucydides Trap'.",
      approx=True),
    T("aristotle", "Aristotle", -384, -322, "Stagira, Chalcidice", "ancient", ["aristotelianism"],
      ["ethics", "metaphysics", "logic", "political-philosophy", "aesthetics", "philosophy-of-science"],
      ["plato", "socrates"],
      "The philosopher who catalogued everything—logic, ethics, biology, politics, poetry.",
      "The son of a court physician in Macedon, Aristotle studied at Plato's Academy for twenty years, later "
      "tutored the young Alexander the Great, and founded his own school, the Lyceum, in Athens. Where Plato "
      "looked upward to ideal Forms, Aristotle looked closely at the world: he systematised formal logic, "
      "classified animals, analysed constitutions and theorised tragedy. His ethics centres on eudaimonia—"
      "flourishing through a life of virtue and reason. Rediscovered in Europe via Arabic scholars, he was simply "
      "'the Philosopher' to medieval thinkers."),
    T("mencius", "Mencius", -372, -289, "State of Zou, China", "ancient", ["confucianism"],
      ["ethics", "political-philosophy"], ["confucius"],
      "The 'Second Sage' of Confucianism, who argued that human nature is good.",
      "Mengzi, known in the West as Mencius, studied in the school of Confucius's grandson and spent years "
      "travelling between the courts of the Warring States, urging rulers to govern through benevolence rather "
      "than force. His central claim—that every person is born with 'sprouts' of compassion, shame, deference and "
      "moral discernment that can be cultivated into virtue—became Confucian orthodoxy. He also argued that a "
      "tyrant who abandons the people loses Heaven's mandate, an early theory of legitimate resistance.",
      approx=True),
    T("zhuangzi", "Zhuangzi", -369, -286, "State of Song, China", "ancient", ["taoism"],
      ["metaphysics", "epistemology", "meaning-of-life"], ["laozi"],
      "Taoist sage of paradox, humour and the butterfly dream.",
      "Zhuang Zhou was a minor official in the state of Song who reportedly turned down a prime ministership, "
      "saying he would rather drag his tail in the mud like a living turtle than be a sacred relic in a temple. "
      "The book bearing his name is full of talking trees, skilled butchers and dreaming butterflies. Through "
      "parable and wit it questions fixed perspectives, rigid morality and the fear of death, inviting readers to "
      "wander freely with the Tao. It is among the great works of Chinese literature as well as philosophy.",
      approx=True),
    T("epicurus", "Epicurus", -341, -270, "Samos", "ancient", ["epicureanism"],
      ["ethics", "metaphysics", "meaning-of-life"], [],
      "Philosopher of the Garden, who taught that a tranquil, pleasant life is the goal.",
      "Epicurus founded a school in a garden outside Athens that, unusually, welcomed women and slaves. He taught "
      "that the universe is made of atoms moving in the void, that the gods do not meddle in human affairs, and "
      "that death is simply the end of sensation and so nothing to fear. The good life is pleasure—but understood "
      "as freedom from pain in the body (aponia) and from disturbance in the mind (ataraxia), achieved through "
      "friendship, simple living and philosophy. 'Epicurean' later came to mean indulgent, which would have puzzled "
      "him: he was content, he said, with bread and water."),
    T("lucretius", "Lucretius", -99, -55, "Probably Rome", "ancient", ["epicureanism"],
      ["metaphysics", "philosophy-of-science", "meaning-of-life"], ["epicurus"],
      "Roman poet who set Epicurean atomism to magnificent verse.",
      "Almost nothing is known about Titus Lucretius Carus beyond his single surviving work, a long Latin poem "
      "addressed to the aristocrat Memmius. Cicero admired its genius and art. Lucretius aimed to free readers "
      "from fear of the gods and of death by explaining the world through atoms, chance and natural law. The poem "
      "nearly vanished during the Middle Ages; its rediscovery by the humanist Poggio Bracciolini in 1417 fed the "
      "scientific and secular imagination of the Renaissance.",
      approx=True),
    T("cicero", "Cicero", -106, -43, "Arpinum, Italy", "ancient", ["stoicism", "skepticism"],
      ["ethics", "political-philosophy"], ["plato", "aristotle", "epicurus"],
      "Roman statesman and orator who brought Greek philosophy into Latin.",
      "Marcus Tullius Cicero rose from a provincial family to become consul of Rome in 63 BCE, when he exposed "
      "the Catiline conspiracy. A defender of the Republic against would-be autocrats, he was sidelined by Caesar "
      "and later murdered on the orders of Mark Antony. In his years out of power he wrote a remarkable series of "
      "philosophical works, coining much of the Latin vocabulary—qualitas, moralis, humanitas—through which Europe "
      "would think. His prose became the model of eloquence for the Renaissance."),
    T("seneca", "Seneca", -4, 65, "Corduba, Hispania", "ancient", ["stoicism"],
      ["ethics", "meaning-of-life"], ["epicurus", "socrates"],
      "Stoic philosopher, playwright and adviser to Nero.",
      "Lucius Annaeus Seneca was a Spanish-born senator, a celebrated dramatist and one of the richest men in "
      "Rome—a fact his critics never let him forget. Exiled to Corsica under Claudius, he was recalled to tutor and "
      "then advise the young Nero, restraining the emperor for some years before withdrawing from court. His "
      "Letters and essays turn Stoicism into practical counsel on anger, grief, friendship, wealth and time. "
      "Accused of conspiracy, he was ordered by Nero to take his own life in 65 CE and did so with deliberate calm.",
      approx=True, dates="c. 4 BCE – 65 CE"),
    T("plutarch", "Plutarch", 46, 119, "Chaeronea, Boeotia", "ancient", ["historiography", "platonism"],
      ["history", "ethics"], ["plato"],
      "Greek biographer whose Parallel Lives taught centuries of readers about character.",
      "Plutarch spent most of his life in his small hometown of Chaeronea, serving as a magistrate and, for many "
      "years, as a priest at the oracle of Delphi. A Platonist philosopher and prodigious writer, he is best known "
      "for the Parallel Lives, paired biographies of Greek and Roman statesmen, and the Moralia, essays on "
      "everything from anger to animal intelligence. His vivid portraits shaped how Europe imagined antiquity: "
      "Shakespeare drew Julius Caesar and Antony and Cleopatra from him, and Montaigne, Rousseau and the American "
      "founders read him closely.",
      approx=True),
    T("epictetus", "Epictetus", 50, 135, "Hierapolis, Phrygia", "ancient", ["stoicism"],
      ["ethics", "meaning-of-life"], ["socrates"],
      "Former slave who became the most influential Stoic teacher.",
      "Epictetus was born into slavery in Phrygia and owned by Epaphroditus, a freedman of Nero; his name simply "
      "means 'acquired'. He studied with the Stoic Musonius Rufus and, after gaining his freedom, taught philosophy "
      "in Rome until the emperor Domitian banished philosophers around 93 CE. He then opened a school at Nicopolis "
      "in Greece. He wrote nothing, but his student Arrian recorded his lectures. Their central lesson—distinguish "
      "what is up to us from what is not—influenced Marcus Aurelius and, in modern times, cognitive behavioural "
      "therapy.",
      approx=True),
    T("marcus-aurelius", "Marcus Aurelius", 121, 180, "Rome", "ancient", ["stoicism"],
      ["ethics", "meaning-of-life"], ["epictetus"],
      "Roman emperor who wrote a private notebook of Stoic self-discipline.",
      "Marcus Aurelius ruled the Roman Empire from 161 to 180, the last of the 'Five Good Emperors'. His reign was "
      "beset by plague and long wars on the Danube frontier, and it was largely in military camps that he wrote, "
      "in Greek, the notes to himself we call the Meditations. Never meant for publication, they record a powerful "
      "man's daily effort to be just, patient and unafraid of death—and to remember that fame, power and pleasure "
      "are fleeting. They remain one of the most widely read works of philosophy."),
    T("nagarjuna", "Nagarjuna", 150, 250, "South India", "ancient", ["buddhism"],
      ["metaphysics", "logic", "epistemology"], ["the-buddha"],
      "Founder of the Madhyamaka 'Middle Way' school of Buddhist philosophy.",
      "Little reliable biography survives for Nagarjuna, who probably lived in South India in the second or third "
      "century CE. He is nonetheless considered by many the most important Buddhist philosopher after the Buddha "
      "himself. With relentless dialectic, he argued that all things are 'empty' (shunya) of independent, "
      "intrinsic existence: they arise only in dependence on causes, parts and concepts. Even emptiness is empty. "
      "His thought became foundational for Mahayana Buddhism in Tibet, China, Korea and Japan.",
      approx=True, dates="c. 2nd–3rd century CE"),
    T("sextus-empiricus", "Sextus Empiricus", 160, 210, "Unknown", "ancient", ["skepticism"],
      ["epistemology", "logic"], [],
      "Physician whose writings preserve ancient Pyrrhonian skepticism.",
      "Sextus Empiricus was a Greek physician of the 'empiric' medical school; beyond that, almost nothing is known "
      "of his life. His writings are our main source for Pyrrhonism, the radical skepticism traced back to Pyrrho "
      "of Elis. Rather than claiming that nothing can be known, the Pyrrhonist balances every argument with an "
      "equally strong counter-argument, suspends judgement, and discovers—unexpectedly—tranquillity. Printed in "
      "Latin translation in the 1560s, Sextus helped spark the skeptical crisis that Montaigne and Descartes "
      "wrestled with.",
      approx=True, dates="fl. c. 200 CE"),
    T("plotinus", "Plotinus", 204, 270, "Lycopolis, Egypt", "ancient", ["neoplatonism"],
      ["metaphysics", "philosophy-of-religion"], ["plato", "aristotle"],
      "Mystic philosopher who founded Neoplatonism.",
      "Born in Roman Egypt, Plotinus studied in Alexandria under the enigmatic Ammonius Saccas, joined an imperial "
      "expedition hoping to learn the wisdom of Persia and India, and finally settled in Rome as a teacher. "
      "According to his student Porphyry, he 'seemed ashamed of being in the body'. His philosophy describes "
      "reality as flowing from a single, ineffable source—the One—through Intellect and Soul down to matter, and "
      "invites the soul to return upward through contemplation. Neoplatonism profoundly shaped Christian, Islamic "
      "and Jewish mysticism and Renaissance thought.",
      approx=True),
    T("augustine", "Augustine of Hippo", 354, 430, "Thagaste, Numidia (present-day Algeria)", "ancient",
      ["christian-philosophy", "neoplatonism"],
      ["philosophy-of-religion", "ethics", "philosophy-of-mind", "history"], ["plato", "plotinus", "cicero"],
      "North African bishop whose writings shaped Christian thought for a millennium.",
      "Aurelius Augustinus was a brilliant, ambitious teacher of rhetoric who drifted through Manichaeism and "
      "skepticism before a dramatic conversion to Christianity in a Milan garden in 386. He returned to Africa, "
      "became bishop of Hippo, and wrote prolifically until his death as the Vandals besieged the city. Augustine "
      "fused Christian faith with Platonist philosophy, and his ideas on grace, original sin, time, memory, the "
      "will and just war became pillars of Western theology. His Confessions essentially invented the "
      "introspective autobiography."),

    # ── Middle Ages ────────────────────────────────────────────────────────
    T("boethius", "Boethius", 477, 524, "Rome", "medieval", ["christian-philosophy", "neoplatonism"],
      ["ethics", "meaning-of-life", "philosophy-of-religion"], ["plato", "aristotle", "augustine"],
      "Roman statesman who wrote philosophy's great prison book.",
      "Anicius Manlius Severinus Boethius was born into one of Rome's leading families shortly after the fall of "
      "the Western Empire. He planned to translate all of Plato and Aristotle into Latin; his versions of "
      "Aristotle's logic were, for centuries, nearly all of Aristotle the Latin West possessed. Rising to the top "
      "of the government of the Ostrogothic king Theodoric, he was accused of treason, imprisoned and executed. "
      "Awaiting death, he wrote The Consolation of Philosophy, among the most copied and translated books of the "
      "Middle Ages.",
      approx=True),
    T("al-farabi", "Al-Farabi", 872, 950, "Central Asia", "medieval", ["islamic-philosophy"],
      ["political-philosophy", "logic", "metaphysics"], ["plato", "aristotle", "plotinus"],
      "The 'Second Teacher' after Aristotle, founder of Islamic political philosophy.",
      "Abu Nasr al-Farabi was probably born in Central Asia and spent most of his career in Baghdad, then an "
      "intellectual capital of the world, before ending his days in Aleppo and Damascus. A logician, music "
      "theorist and commentator, he was so respected as an interpreter of Aristotle that he was called 'the Second "
      "Teacher'. He fused Aristotelian logic and Neoplatonic cosmology with a Platonic vision of politics in which "
      "the ideal ruler is a philosopher-prophet guiding citizens to happiness. Avicenna said he only understood "
      "Aristotle's Metaphysics after reading al-Farabi.",
      approx=True),
    T("avicenna", "Avicenna (Ibn Sina)", 980, 1037, "Afshana, near Bukhara", "medieval", ["islamic-philosophy"],
      ["metaphysics", "philosophy-of-mind", "logic", "philosophy-of-science"], ["aristotle", "al-farabi"],
      "Persian polymath whose medicine and metaphysics shaped East and West.",
      "Abu Ali al-Husayn ibn Sina was a prodigy who, by his own account, had mastered medicine by sixteen. He "
      "served as physician and vizier to a series of Persian rulers, often writing on the move or in hiding during "
      "political upheavals. His Canon of Medicine was a standard textbook in Europe for some five centuries. In "
      "philosophy, his distinction between essence and existence, his proof of a Necessary Existent, and his "
      "'floating man' thought experiment—a mind aware of itself without any bodily sensation—profoundly "
      "influenced Aquinas and anticipated Descartes."),
    T("anselm", "Anselm of Canterbury", 1033, 1109, "Aosta, Italy", "medieval",
      ["scholasticism", "christian-philosophy"], ["philosophy-of-religion", "metaphysics"], ["augustine"],
      "Archbishop of Canterbury and author of the ontological argument for God.",
      "Born in the Alpine town of Aosta, Anselm became a monk and then abbot at Bec in Normandy, and in 1093 "
      "Archbishop of Canterbury, where he clashed repeatedly with English kings over the rights of the Church. His "
      "motto, 'faith seeking understanding', captures his project of using reason to illuminate what he already "
      "believed. In the Proslogion he proposed that God is 'that than which nothing greater can be conceived', and "
      "that such a being must exist in reality, not merely in the mind—an argument philosophers still dispute."),
    T("al-ghazali", "Al-Ghazali", 1058, 1111, "Tus, Persia", "medieval", ["islamic-philosophy"],
      ["philosophy-of-religion", "epistemology", "meaning-of-life"], ["avicenna", "al-farabi"],
      "Theologian and mystic who put philosophy itself on trial.",
      "Abu Hamid al-Ghazali was the star professor at the prestigious Nizamiyya college in Baghdad when, in 1095, a "
      "spiritual crisis left him unable to speak. He abandoned his post, lived as a wandering Sufi and spent years "
      "in retreat before returning to teaching. In The Incoherence of the Philosophers he used rigorous logic to "
      "attack Avicenna's claims that the world is eternal and that God knows only universals. He argued that "
      "causation is not a necessary link but a regularity God sustains—an idea often compared to Hume. He remains "
      "one of the most influential thinkers in Islamic history.",
      approx=True),
    T("averroes", "Averroes (Ibn Rushd)", 1126, 1198, "Córdoba, al-Andalus", "medieval",
      ["islamic-philosophy", "aristotelianism"], ["metaphysics", "philosophy-of-religion", "philosophy-of-science"],
      ["aristotle", "avicenna", "al-ghazali"],
      "Andalusian judge known to Europe simply as 'the Commentator' on Aristotle.",
      "Abu al-Walid ibn Rushd came from a family of eminent judges in Córdoba and served as chief judge and court "
      "physician under the Almohad caliphs. Commissioned to explain Aristotle, he wrote commentaries so thorough "
      "that Latin scholars called him simply 'the Commentator'. He defended philosophy against al-Ghazali, and "
      "argued that reason and revelation cannot truly conflict and that philosophical study is in fact commanded "
      "for those able to pursue it. Late in life he fell from favour and his books were burned, but 'Averroism' "
      "became a major current in European universities."),
    T("maimonides", "Maimonides", 1138, 1204, "Córdoba, al-Andalus", "medieval",
      ["jewish-philosophy", "aristotelianism"], ["philosophy-of-religion", "ethics", "metaphysics"],
      ["aristotle", "al-farabi"],
      "Rabbi, physician and philosopher who reconciled Torah with Aristotle.",
      "Moses ben Maimon was born in Córdoba, but persecution under the Almohads drove his family to Morocco and "
      "eventually to Egypt, where he became a leader of the Jewish community and a court physician. His Mishneh "
      "Torah systematised all of Jewish law, and his Guide for the Perplexed addressed educated believers torn "
      "between scripture and philosophy. Insisting that God is utterly beyond human description, he argued that "
      "we can speak of God truly only by saying what God is not. A popular saying runs: 'From Moses to Moses there "
      "was none like Moses.'"),
    T("dogen", "Dōgen", 1200, 1253, "Kyoto, Japan", "medieval", ["buddhism"],
      ["metaphysics", "meaning-of-life"], ["the-buddha", "nagarjuna"],
      "Founder of Sōtō Zen and one of Japan's most original philosophers.",
      "Orphaned young, Eihei Dōgen became a monk on Mount Hiei and, troubled by the question of why practice is "
      "needed if all beings already have Buddha-nature, travelled to China in 1223. There he studied under the "
      "Chan master Rujing and experienced awakening. Back in Japan he founded the Sōtō school of Zen and the "
      "monastery of Eiheiji. He taught shikantaza—'just sitting'—as itself the expression of enlightenment, not a "
      "means to it. His essays on time, being and language are now read alongside Heidegger and Wittgenstein."),
    T("thomas-aquinas", "Thomas Aquinas", 1225, 1274, "Roccasecca, Kingdom of Sicily", "medieval",
      ["scholasticism", "aristotelianism", "christian-philosophy"],
      ["philosophy-of-religion", "ethics", "metaphysics", "political-philosophy"],
      ["aristotle", "augustine", "avicenna", "averroes", "maimonides"],
      "Dominican friar whose synthesis of Aristotle and Christianity defined scholasticism.",
      "Born to a noble family so opposed to his joining the mendicant Dominican order that his brothers reportedly "
      "held him captive for a year, Thomas Aquinas went on to study under Albert the Great and teach at the "
      "University of Paris. Nicknamed 'the Dumb Ox' for his quiet bulk, he wrote millions of words, aiming to show "
      "that faith and reason are complementary. His Five Ways argue for God's existence, his natural law theory "
      "grounds ethics in human nature, and his criteria for just war are still cited. Shortly before his death he "
      "had an experience after which all he had written seemed to him 'like straw'."),
    T("william-of-ockham", "William of Ockham", 1287, 1347, "Ockham, Surrey", "medieval", ["scholasticism"],
      ["logic", "metaphysics", "epistemology", "political-philosophy"], ["aristotle", "thomas-aquinas"],
      "Franciscan logician remembered for 'Ockham's razor'.",
      "A Franciscan friar educated at Oxford, William of Ockham was summoned to the papal court at Avignon to "
      "answer charges of heresy. There he sided with Franciscans who held that Christ and the apostles owned no "
      "property, denounced Pope John XXII as a heretic, and fled to the protection of Emperor Louis IV in Munich. "
      "As a philosopher he championed nominalism—only individual things exist; universals are just concepts or "
      "names—and a principle of parsimony that became known as Ockham's razor: do not multiply entities beyond "
      "necessity.",
      approx=True),
    T("ibn-khaldun", "Ibn Khaldun", 1332, 1406, "Tunis", "medieval", ["historiography", "islamic-philosophy"],
      ["history", "society-and-economics", "political-philosophy"], ["aristotle"],
      "North African historian who founded a science of society.",
      "Born in Tunis to a family of Andalusian origin, Ibn Khaldun lived a turbulent career as a diplomat, judge "
      "and courtier in North Africa, Granada and Mamluk Cairo; in 1401 he even met the conqueror Timur outside "
      "Damascus. Retreating to a castle in present-day Algeria in 1375, he wrote the Muqaddimah, an introduction to "
      "history that sought the underlying causes of the rise and fall of states. Analysing group solidarity "
      "(asabiyya), economics and the contrast between nomadic and urban life, he is often called a founder of "
      "sociology, economics and the philosophy of history."),

    # ── Renaissance ────────────────────────────────────────────────────────
    T("erasmus", "Desiderius Erasmus", 1466, 1536, "Rotterdam", "renaissance",
      ["renaissance-humanism", "christian-philosophy"], ["ethics", "philosophy-of-religion"],
      ["plato", "plutarch", "cicero"],
      "Prince of the humanists, scholar and satirist of a corrupt age.",
      "Desiderius Erasmus was the illegitimate son of a priest, educated in monastic schools he later remembered "
      "with distaste. Ordained but unwilling to stay in the cloister, he became the most famous scholar in Europe, "
      "corresponding with popes and kings and moving between Paris, England, Italy and Basel. He edited the first "
      "published Greek New Testament, collected thousands of classical proverbs, and championed a simple, inward "
      "Christianity and peace among nations. He criticised Church abuses but refused to join Luther's Reformation, "
      "earning suspicion from both sides.",
      approx=True),
    T("machiavelli", "Niccolò Machiavelli", 1469, 1527, "Florence", "renaissance",
      ["political-realism", "renaissance-humanism"], ["political-philosophy", "history"],
      ["lucretius", "thucydides", "plutarch"],
      "Florentine diplomat whose clear-eyed account of power made his name a byword.",
      "Niccolò Machiavelli served the Florentine Republic for fourteen years as a diplomat and secretary, meeting "
      "Cesare Borgia, popes and the king of France. When the Medici returned to power in 1512 he was dismissed, "
      "imprisoned and tortured. In exile on his farm he wrote The Prince, a handbook on gaining and keeping power "
      "that sets aside how rulers ought to behave in favour of how they actually do. He also wrote the Discourses "
      "on Livy, a sustained defence of republics, as well as plays and a history of Florence. Whether he was a "
      "cynic, a satirist or a patriot is still debated."),
    T("wang-yangming", "Wang Yangming", 1472, 1529, "Yuyao, Zhejiang, China", "renaissance",
      ["neo-confucianism"], ["ethics", "epistemology"], ["confucius", "mencius"],
      "Ming statesman-philosopher who taught the unity of knowledge and action.",
      "Wang Shouren, known by his literary name Yangming, was a scholar-official, general and one of the most "
      "influential Confucian thinkers of the last millennium. Banished to a remote post in Guizhou after offending "
      "a powerful eunuch, he had an awakening: the principles of things are not found by investigating external "
      "objects but are present in the mind itself. He taught that everyone possesses innate moral knowledge "
      "(liangzhi) and that true knowledge is inseparable from action. His school deeply influenced thinkers in "
      "Japan and Korea."),
    T("thomas-more", "Thomas More", 1478, 1535, "London", "renaissance",
      ["renaissance-humanism", "christian-philosophy"], ["political-philosophy", "ethics"], ["plato", "erasmus"],
      "Humanist, Lord Chancellor of England and author of Utopia.",
      "A London lawyer, close friend of Erasmus and accomplished classical scholar, Thomas More rose to become Lord "
      "Chancellor under Henry VIII. In 1516 he published Utopia, coining a word that puns on 'no place' and 'good "
      "place'. When Henry broke with Rome, More refused to swear the oath acknowledging the king as head of the "
      "Church in England and was beheaded for treason in 1535, reportedly declaring himself 'the king's good "
      "servant, but God's first'. He was canonised by the Catholic Church in 1935."),
    T("montaigne", "Michel de Montaigne", 1533, 1592, "Château de Montaigne, Périgord", "renaissance",
      ["renaissance-humanism", "skepticism"], ["ethics", "epistemology", "meaning-of-life"],
      ["seneca", "plutarch", "sextus-empiricus", "lucretius", "socrates"],
      "French nobleman who invented the essay by making himself his subject.",
      "Michel de Montaigne was raised to speak Latin before French, served as a magistrate in Bordeaux, and at 38 "
      "retired to a tower library in his château to read and think. The result was the Essays—'attempts'—in which "
      "he examined cannibals, friendship, cruelty, idleness, his kidney stones and his own changing mind, believing "
      "that 'each man bears the entire form of the human condition'. Skeptical, tolerant and endlessly curious, he "
      "wrote during the French Wars of Religion yet counselled humility over certainty. Shakespeare, Pascal, "
      "Emerson and Nietzsche were among his devoted readers."),
    T("francis-bacon", "Francis Bacon", 1561, 1626, "London", "renaissance", ["empiricism"],
      ["philosophy-of-science", "epistemology"], ["aristotle", "lucretius"],
      "English statesman who championed experiment and induction as the path to knowledge.",
      "Francis Bacon combined a dazzling legal and political career—he became Lord Chancellor under James I—with a "
      "grand ambition to reform all of human knowledge. He argued that learning had stagnated because scholars "
      "deferred to Aristotle and reasoned from first principles instead of patiently gathering observations and "
      "testing them. Knowledge should be useful, 'for the relief of man's estate'. His career ended in disgrace in "
      "1621 after he admitted taking bribes, and legend says he died from a chill caught while stuffing a chicken "
      "with snow to test refrigeration. The founders of the Royal Society hailed him as their inspiration."),

    # ── Early Modern & Enlightenment ───────────────────────────────────────
    T("thomas-hobbes", "Thomas Hobbes", 1588, 1679, "Westport, Malmesbury, England", "early-modern",
      ["social-contract", "political-realism"], ["political-philosophy", "philosophy-of-mind"],
      ["thucydides", "francis-bacon", "aristotle"],
      "English philosopher who argued that only a sovereign can save us from a war of all against all.",
      "Thomas Hobbes said that his mother gave birth to twins—himself and fear—when news of the approaching Spanish "
      "Armada brought on her labour. He translated Thucydides, served the Cavendish family as tutor, met Galileo, "
      "and fled to Paris on the eve of the English Civil War. Impressed by geometry, he tried to build a science of "
      "politics from the ground up: humans are matter in motion, driven by appetite and fear, and without a common "
      "power to keep them in awe they would be in a 'war of every man against every man'. He lived to 91, "
      "translating Homer in his eighties."),
    T("rene-descartes", "René Descartes", 1596, 1650, "La Haye en Touraine, France", "early-modern",
      ["rationalism"], ["epistemology", "metaphysics", "philosophy-of-mind", "philosophy-of-science"],
      ["augustine", "aristotle", "montaigne"],
      "Father of modern philosophy, who doubted everything to find what could not be doubted.",
      "Educated by Jesuits, René Descartes served as a gentleman soldier and, in 1619, had a series of dreams that "
      "convinced him to rebuild knowledge on certain foundations. He spent most of his career in the Netherlands, "
      "contributing to optics and inventing the coordinate geometry that bears his name. His method of radical "
      "doubt led to the one certainty, 'I think, therefore I am', and to a sharp distinction between mind and body "
      "that philosophers of mind still argue about. Invited to Stockholm to tutor Queen Christina at five in the "
      "morning, he died of pneumonia within months."),
    T("blaise-pascal", "Blaise Pascal", 1623, 1662, "Clermont-Ferrand, France", "early-modern",
      ["christian-philosophy"], ["philosophy-of-religion", "meaning-of-life", "epistemology"],
      ["montaigne", "augustine", "rene-descartes"],
      "Mathematician and mystic who weighed the human condition between infinity and nothingness.",
      "A child prodigy, Blaise Pascal built one of the first mechanical calculators as a teenager, did foundational "
      "work on probability with Fermat, and conducted famous experiments on the vacuum and air pressure. In "
      "November 1654 he had an intense religious experience—recorded on a scrap of parchment he kept sewn into his "
      "coat—and thereafter devoted himself to defending Christianity, aligned with the austere Jansenists of "
      "Port-Royal. He died at 39, leaving notes for an apology for the faith that were published as the Pensées."),
    T("baruch-spinoza", "Baruch Spinoza", 1632, 1677, "Amsterdam", "early-modern", ["rationalism"],
      ["metaphysics", "ethics", "philosophy-of-religion", "political-philosophy"],
      ["rene-descartes", "maimonides", "thomas-hobbes"],
      "Lens grinder who identified God with Nature and freedom with understanding.",
      "Baruch Spinoza was born to a family of Portuguese-Jewish merchants in Amsterdam and, at 23, was expelled "
      "from the synagogue with an unusually severe writ of excommunication. He lived modestly, grinding optical "
      "lenses, and declined a professorship at Heidelberg to protect his independence. His Theological-Political "
      "Treatise defended freedom of thought and read the Bible as a historical document; it was banned. His Ethics, "
      "published after his death, argues that there is one infinite substance—'God, or Nature'—and that human "
      "freedom lies in understanding the causes that move us. Einstein said he believed in 'Spinoza's God'."),
    T("john-locke", "John Locke", 1632, 1704, "Wrington, Somerset", "early-modern",
      ["empiricism", "social-contract", "liberalism"], ["political-philosophy", "epistemology", "philosophy-of-mind"],
      ["rene-descartes", "thomas-hobbes", "francis-bacon"],
      "Founder of liberalism, who grounded government in consent and knowledge in experience.",
      "Trained as a physician at Oxford, John Locke became adviser to the Earl of Shaftesbury, a leader of "
      "opposition to the Stuart kings, and spent years in exile in the Netherlands. He returned after the Glorious "
      "Revolution of 1688 and published in quick succession his Essay Concerning Human Understanding, his Two "
      "Treatises of Government and a Letter Concerning Toleration. The mind, he argued, begins as a blank slate "
      "written on by experience; governments exist to protect life, liberty and property, and when they betray "
      "that trust the people may resist. His ideas echo through the American Declaration of Independence."),
    T("leibniz", "Gottfried Wilhelm Leibniz", 1646, 1716, "Leipzig", "early-modern", ["rationalism"],
      ["metaphysics", "logic", "philosophy-of-religion"], ["rene-descartes", "baruch-spinoza", "aristotle"],
      "Universal genius who co-invented calculus and imagined a world of monads.",
      "Gottfried Wilhelm Leibniz was a diplomat, librarian, lawyer and engineer who also independently invented "
      "calculus (leading to a bitter priority dispute with Newton), designed a calculating machine, and dreamed of a "
      "universal logical language in which disputes could be settled by saying 'Let us calculate'. His metaphysics "
      "pictures reality as made of simple, mind-like substances—monads—coordinated by a pre-established harmony. "
      "He argued that God created the best of all possible worlds, a claim Voltaire mercilessly satirised in "
      "Candide."),
    T("george-berkeley", "George Berkeley", 1685, 1753, "Kilkenny, Ireland", "early-modern", ["empiricism"],
      ["metaphysics", "epistemology"], ["john-locke", "rene-descartes"],
      "Irish bishop who argued that matter does not exist—only minds and ideas.",
      "George Berkeley was a young fellow of Trinity College Dublin when he published his most radical works, "
      "arguing that 'to be is to be perceived' (esse est percipi): the objects we know are collections of ideas, "
      "and there is no unperceived material substance behind them. The world persists when we look away because "
      "it is always perceived by God. He later spent three years in Rhode Island trying to found a college in "
      "Bermuda, became Bishop of Cloyne, and promoted tar-water as a cure-all. The city of Berkeley, California, "
      "is named after him."),
    T("montesquieu", "Montesquieu", 1689, 1755, "La Brède, near Bordeaux", "early-modern",
      ["enlightenment", "liberalism"], ["political-philosophy", "society-and-economics"], ["john-locke", "cicero"],
      "French jurist who taught the world to separate powers.",
      "Charles-Louis de Secondat, Baron de Montesquieu, inherited a seat in the Bordeaux parlement and a vineyard. "
      "He first won fame with the Persian Letters, a satire of French society seen through the eyes of two Persian "
      "visitors. After years of travel, including a long stay in England, he published The Spirit of the Laws in "
      "1748, comparing governments across history and climates. His argument that liberty requires separating "
      "legislative, executive and judicial power became a cornerstone of the United States Constitution."),
    T("voltaire", "Voltaire", 1694, 1778, "Paris", "early-modern", ["enlightenment"],
      ["philosophy-of-religion", "political-philosophy", "ethics"], ["john-locke", "leibniz", "montaigne"],
      "Wit, playwright and crusader for tolerance who embodied the French Enlightenment.",
      "François-Marie Arouet, who wrote as Voltaire, was imprisoned in the Bastille for satirical verses, exiled to "
      "England—where he admired Newton, Locke and religious tolerance—and spent decades dodging censors from "
      "estates near the Swiss border. He wrote plays, histories, poems, a philosophical dictionary and some twenty "
      "thousand letters. He campaigned to clear the name of Jean Calas, a Protestant tortured and executed on false "
      "charges, making his cry 'Écrasez l'infâme' ('Crush the infamous thing') a rallying call against fanaticism."),
    T("david-hume", "David Hume", 1711, 1776, "Edinburgh", "early-modern", ["empiricism", "enlightenment"],
      ["epistemology", "ethics", "philosophy-of-religion", "philosophy-of-mind"], ["john-locke", "george-berkeley"],
      "Scottish skeptic who woke Kant from his dogmatic slumber.",
      "David Hume published his Treatise of Human Nature in his twenties; it 'fell dead-born from the press'. He "
      "found fame instead as an essayist and as author of a bestselling History of England, though his reputation "
      "for irreligion cost him professorships at Edinburgh and Glasgow. His philosophy pushes empiricism to its "
      "limits: we never observe causation, only constant conjunction; the self is a bundle of perceptions; and "
      "reason alone cannot motivate action. Genial and much-loved—Parisian salons called him 'le bon David'—he "
      "faced death with a cheerfulness that astonished James Boswell."),
    T("jean-jacques-rousseau", "Jean-Jacques Rousseau", 1712, 1778, "Geneva", "early-modern",
      ["social-contract", "enlightenment"], ["political-philosophy", "ethics", "society-and-economics"],
      ["thomas-hobbes", "john-locke", "plato", "montaigne"],
      "Genevan outsider who blamed society for our chains and imagined a democracy of the general will.",
      "Jean-Jacques Rousseau's mother died days after his birth; he left Geneva at fifteen and lived as an "
      "apprentice, servant, music copyist and composer. In 1750 he won an essay prize by arguing, against the "
      "spirit of the age, that the arts and sciences had corrupted morals. His works on inequality, the social "
      "contract and education (Emile) were condemned and burned, forcing him to flee. Prickly, suspicious and "
      "visionary, he inspired both the French revolutionaries and the Romantic movement—and placed his own five "
      "children in a foundling hospital, a fact that has troubled readers ever since."),
    T("adam-smith", "Adam Smith", 1723, 1790, "Kirkcaldy, Scotland", "early-modern",
      ["enlightenment", "liberalism"], ["society-and-economics", "ethics"], ["david-hume"],
      "Moral philosopher who founded modern economics.",
      "Adam Smith was professor of moral philosophy at Glasgow and a close friend of David Hume. His first book, "
      "The Theory of Moral Sentiments, grounds morality in sympathy and the imagined judgement of an 'impartial "
      "spectator'. After touring France as tutor to a young duke and meeting the physiocrats, he spent a decade "
      "writing The Wealth of Nations, which explains how the division of labour and free exchange create "
      "prosperity. Often caricatured as a prophet of greed, Smith was in fact wary of merchants' collusion and "
      "deeply concerned with the moral health of commercial society."),
    T("immanuel-kant", "Immanuel Kant", 1724, 1804, "Königsberg, Prussia", "early-modern",
      ["german-idealism", "enlightenment"], ["epistemology", "metaphysics", "ethics", "aesthetics",
                                             "political-philosophy"],
      ["david-hume", "leibniz", "jean-jacques-rousseau"],
      "Königsberg professor who reshaped philosophy with his Copernican revolution.",
      "Immanuel Kant never travelled far from Königsberg, and his daily walk was reputedly so regular that "
      "neighbours could set their clocks by it. Yet from that quiet life came a revolution. Roused by Hume's "
      "skepticism, he argued that the mind does not passively receive the world but actively structures "
      "experience through space, time and categories such as causality. In ethics he grounded morality in reason "
      "itself: act only on principles you could will to be universal laws, and treat humanity always as an end, "
      "never merely as a means. His essay on perpetual peace foreshadowed the League of Nations."),
    T("edmund-burke", "Edmund Burke", 1729, 1797, "Dublin", "early-modern", ["conservatism"],
      ["political-philosophy", "aesthetics"], ["montesquieu", "cicero"],
      "Irish statesman regarded as the founder of modern conservatism.",
      "Edmund Burke moved from Dublin to London to study law, made his name with a treatise on the sublime and the "
      "beautiful, and sat in Parliament for nearly thirty years as a Whig. He supported conciliation with the "
      "American colonists, campaigned against corruption in British India, and pressed for relief for Irish "
      "Catholics. Yet his fierce opposition to the French Revolution, which he predicted would end in terror and "
      "military dictatorship, made him the intellectual father of conservatism: society is a partnership between "
      "the dead, the living and the unborn, and should be reformed gradually rather than torn down."),
    T("edward-gibbon", "Edward Gibbon", 1737, 1794, "Putney, Surrey", "early-modern",
      ["historiography", "enlightenment"], ["history"], ["montesquieu", "voltaire", "david-hume"],
      "English historian of Rome's decline and fall.",
      "Edward Gibbon was a sickly child whose education was largely self-directed; a youthful conversion to "
      "Catholicism led his father to pack him off to Lausanne, where he returned to Protestantism and absorbed "
      "French culture. Musing amid the ruins of the Capitol in Rome in 1764, he conceived the idea of writing the "
      "history of the city's decline. The six volumes, published between 1776 and 1789, cover more than a thousand "
      "years. Their irony, erudition and magnificent prose—and their treatment of early Christianity—made them a "
      "sensation and a scandal."),
    T("thomas-paine", "Thomas Paine", 1737, 1809, "Thetford, England", "early-modern",
      ["enlightenment", "liberalism"], ["political-philosophy"], ["john-locke", "jean-jacques-rousseau"],
      "Pamphleteer whose words helped ignite the American and French revolutions.",
      "Thomas Paine was a failed corset-maker and dismissed excise officer when he emigrated to America in 1774 "
      "with a letter of introduction from Benjamin Franklin. Within two years he had published Common Sense, the "
      "most widely read pamphlet of the American Revolution. He went on to defend the French Revolution in Rights "
      "of Man, was elected to the French National Convention, opposed the execution of Louis XVI and narrowly "
      "escaped the guillotine himself. His deist Age of Reason made him a pariah, and only a handful of people "
      "attended his funeral."),
    T("mary-wollstonecraft", "Mary Wollstonecraft", 1759, 1797, "London", "early-modern",
      ["enlightenment", "feminism", "liberalism"], ["political-philosophy", "ethics"],
      ["jean-jacques-rousseau", "john-locke"],
      "Pioneer of feminist philosophy who demanded education and reason for women.",
      "Mary Wollstonecraft grew up with a violent, spendthrift father and supported herself as a companion, "
      "governess, schoolteacher and finally a professional writer in radical London circles. She answered Burke "
      "with A Vindication of the Rights of Men and then, in 1792, wrote A Vindication of the Rights of Woman, "
      "arguing that women only appear inferior because they are denied education. She witnessed the Terror in "
      "Paris, survived two suicide attempts, married the philosopher William Godwin, and died days after giving "
      "birth to Mary Shelley, the future author of Frankenstein."),

    # ── Nineteenth century ─────────────────────────────────────────────────
    T("hegel", "G. W. F. Hegel", 1770, 1831, "Stuttgart", "modern", ["german-idealism"],
      ["metaphysics", "history", "political-philosophy"],
      ["immanuel-kant", "baruch-spinoza", "aristotle", "plato", "jean-jacques-rousseau"],
      "Philosopher of Spirit, dialectic and history's rational unfolding.",
      "Georg Wilhelm Friedrich Hegel roomed at the Tübingen seminary with the poet Hölderlin and the philosopher "
      "Schelling, and finished his first great book, the Phenomenology of Spirit, in Jena in 1806 as Napoleon's "
      "armies arrived—he glimpsed the emperor riding through town, 'the world-soul on horseback'. He later held "
      "the chair of philosophy in Berlin and became the dominant philosopher in Germany. For Hegel, reality is the "
      "self-development of Spirit, and history is the story of freedom coming to know itself through conflict and "
      "reconciliation. Both Marx and his conservative opponents claimed his inheritance."),
    T("arthur-schopenhauer", "Arthur Schopenhauer", 1788, 1860, "Danzig", "modern", ["german-idealism"],
      ["metaphysics", "aesthetics", "ethics", "meaning-of-life"], ["immanuel-kant", "plato", "the-buddha"],
      "Pessimist who saw a blind, striving Will behind everything.",
      "The son of a wealthy merchant and a popular novelist, Arthur Schopenhauer published his masterpiece at "
      "thirty and then waited decades for anyone to notice. As a Berlin lecturer he scheduled his classes against "
      "Hegel's, and almost no students came. He argued that the world as we experience it is representation, "
      "while its inner nature is a restless, irrational Will that dooms us to oscillate between suffering and "
      "boredom. Relief comes through art—above all music—compassion and ascetic renunciation, ideas he found echoed "
      "in Hindu and Buddhist texts. Fame arrived in his final decade, and he influenced Wagner, Nietzsche, Freud "
      "and Wittgenstein."),
    T("ralph-waldo-emerson", "Ralph Waldo Emerson", 1803, 1882, "Boston", "modern", ["transcendentalism"],
      ["ethics", "philosophy-of-religion", "meaning-of-life"], ["montaigne", "plato", "immanuel-kant"],
      "Sage of Concord who preached self-reliance and the divinity of nature.",
      "Ralph Waldo Emerson resigned as a Unitarian minister in 1832 because he could no longer in conscience "
      "administer communion. After travelling in Europe and meeting Coleridge, Wordsworth and Carlyle, he settled "
      "in Concord, Massachusetts, and launched Transcendentalism with his essay Nature (1836). His lectures and "
      "essays called on Americans to trust their own intuition, to stop imitating Europe, and to find the divine in "
      "nature and the self. He mentored Thoreau, championed Walt Whitman, and profoundly influenced Nietzsche."),
    T("alexis-de-tocqueville", "Alexis de Tocqueville", 1805, 1859, "Paris", "modern",
      ["liberalism", "historiography"], ["political-philosophy", "history", "society-and-economics"],
      ["montesquieu", "jean-jacques-rousseau"],
      "French aristocrat who saw democracy's promise and perils in America.",
      "Alexis de Tocqueville came from a Norman aristocratic family that had lost members to the guillotine. In "
      "1831 he and his friend Gustave de Beaumont sailed to the United States, officially to study prisons. Over "
      "nine months they travelled from New England to New Orleans, and the result was Democracy in America, a "
      "penetrating study of a society built on equality of conditions. Tocqueville later served as a deputy and "
      "briefly as French foreign minister, and wrote The Old Regime and the Revolution, arguing that the Revolution "
      "continued centralising trends begun under the monarchy."),
    T("john-stuart-mill", "John Stuart Mill", 1806, 1873, "London", "modern",
      ["utilitarianism", "liberalism", "feminism"],
      ["ethics", "political-philosophy", "logic", "society-and-economics"],
      ["alexis-de-tocqueville", "adam-smith", "david-hume", "mary-wollstonecraft"],
      "Liberal philosopher of freedom, utility and equality.",
      "John Stuart Mill was subjected by his father to an extraordinary education—Greek at three, Latin at eight—"
      "intended to make him a champion of Jeremy Bentham's utilitarianism. At twenty he suffered a breakdown and "
      "found healing in Wordsworth's poetry, which deepened his sense of what makes life valuable. He worked for the "
      "East India Company, served as a Member of Parliament—where in 1867 he proposed giving women the vote—and "
      "wrote influential works on logic, economics and ethics. He credited his wife, Harriet Taylor, as a "
      "partner in much of his thought."),
    T("soren-kierkegaard", "Søren Kierkegaard", 1813, 1855, "Copenhagen", "modern",
      ["existentialism", "christian-philosophy"], ["philosophy-of-religion", "meaning-of-life", "ethics"],
      ["socrates", "hegel"],
      "Danish thinker of anxiety, faith and the individual: the father of existentialism.",
      "Søren Kierkegaard was the youngest son of a wealthy, melancholic Copenhagen merchant. He broke off his "
      "engagement to Regine Olsen—an event that haunted his work—and poured himself into a torrent of books, many "
      "under pseudonyms that represent different ways of life. Against Hegel's grand system and Denmark's "
      "comfortable state church, he insisted that truth is subjectivity: what matters is how a single individual "
      "lives, chooses and believes, in fear and trembling, before God. He died at 42, little read outside Denmark; "
      "in the twentieth century he was hailed as the first existentialist."),
    T("henry-david-thoreau", "Henry David Thoreau", 1817, 1862, "Concord, Massachusetts", "modern",
      ["transcendentalism"], ["ethics", "political-philosophy", "meaning-of-life"], ["ralph-waldo-emerson"],
      "Naturalist and dissenter who lived deliberately at Walden Pond.",
      "Henry David Thoreau, a Harvard graduate who worked as a surveyor and in his family's pencil business, was a "
      "protégé of Emerson. In 1845 he built a cabin on Emerson's land at Walden Pond and lived there for two "
      "years, two months and two days, an experiment in simple living that became Walden. A night in jail for "
      "refusing to pay a poll tax that supported slavery and the Mexican–American War produced his essay on civil "
      "disobedience, later an inspiration to Tolstoy, Gandhi and Martin Luther King Jr."),
    T("karl-marx", "Karl Marx", 1818, 1883, "Trier, Prussia", "modern", ["marxism"],
      ["political-philosophy", "society-and-economics", "history"],
      ["hegel", "adam-smith", "jean-jacques-rousseau"],
      "Revolutionary theorist of capitalism, class struggle and history.",
      "Karl Marx studied law and philosophy, edited a radical newspaper in Cologne until it was suppressed, and was "
      "expelled from Paris and Brussels before settling, poor and stateless, in London in 1849. With his lifelong "
      "collaborator Friedrich Engels he wrote The Communist Manifesto; in the British Museum reading room he spent "
      "decades on Capital, a critique of political economy. He argued that history is driven by conflict between "
      "classes over material production and that capitalism would be overthrown by the workers it exploited. Few "
      "thinkers have had a greater impact on the twentieth century."),
    T("fyodor-dostoevsky", "Fyodor Dostoevsky", 1821, 1881, "Moscow", "modern",
      ["existentialism", "christian-philosophy"], ["meaning-of-life", "philosophy-of-religion", "ethics"], [],
      "Russian novelist who dramatised freedom, faith and the underground man.",
      "Fyodor Dostoevsky was arrested in 1849 for belonging to a radical discussion circle, sentenced to death, and "
      "reprieved only at the last moment in front of the firing squad. He served four years of hard labour in "
      "Siberia, an experience that transformed his faith. Plagued by epilepsy, gambling debts and grief, he wrote "
      "novels—Crime and Punishment, The Idiot, Demons, The Brothers Karamazov—that stage philosophical arguments "
      "between living characters. Nietzsche called him 'the only psychologist from whom I had something to learn'."),
    T("william-james", "William James", 1842, 1910, "New York City", "modern", ["pragmatism"],
      ["epistemology", "philosophy-of-mind", "philosophy-of-religion"],
      ["ralph-waldo-emerson", "john-stuart-mill"],
      "American pioneer of psychology and pragmatism.",
      "Brother of the novelist Henry James, William James trained as a painter and then a physician, suffered a "
      "long depression in his twenties, and recovered partly by deciding that his 'first act of free will shall be "
      "to believe in free will'. At Harvard he taught the first psychology course in America and wrote The "
      "Principles of Psychology, popularising the phrase 'stream of consciousness'. His pragmatism holds that the "
      "meaning and truth of an idea lie in its practical consequences, and his studies of religious experience "
      "remain classics."),
    T("friedrich-nietzsche", "Friedrich Nietzsche", 1844, 1900, "Röcken, Prussia", "modern", ["existentialism"],
      ["ethics", "meaning-of-life", "philosophy-of-religion", "aesthetics"],
      ["arthur-schopenhauer", "ralph-waldo-emerson", "heraclitus", "fyodor-dostoevsky"],
      "Philosopher with a hammer who announced the death of God and the task of creating values.",
      "Friedrich Nietzsche was appointed professor of classical philology at Basel at just 24. Ill health forced "
      "him to retire a decade later, and he spent the 1880s wandering between Swiss mountain villages and Italian "
      "towns, writing at an astonishing pace. He diagnosed a crisis in European culture: with the 'death of God', "
      "the foundations of morality had collapsed, threatening nihilism. His answer was to re-evaluate all values, "
      "to affirm life as it is, and to become who you are. In January 1889 he collapsed in Turin and never "
      "recovered his sanity. His sister later distorted his work in the service of German nationalism, a "
      "falsification scholars have since undone."),

    # ── Twentieth century & today ──────────────────────────────────────────
    T("edmund-husserl", "Edmund Husserl", 1859, 1938, "Prossnitz, Moravia", "contemporary", ["phenomenology"],
      ["epistemology", "philosophy-of-mind"], ["rene-descartes", "immanuel-kant"],
      "Founder of phenomenology, the science of experience itself.",
      "Edmund Husserl began as a mathematician before turning to philosophy under the influence of Franz Brentano. "
      "In works such as the Logical Investigations (1900–01) he launched phenomenology: rather than speculate about "
      "what lies behind appearances, describe precisely how things show up in consciousness—'back to the things "
      "themselves'. He taught at Göttingen and Freiburg, where Heidegger was his assistant and successor. Born to "
      "a Jewish family, he was excluded from his university under the Nazis; after his death his tens of thousands "
      "of manuscript pages were smuggled to Leuven for safekeeping."),
    T("web-du-bois", "W. E. B. Du Bois", 1868, 1963, "Great Barrington, Massachusetts", "contemporary",
      ["anticolonial-thought", "pragmatism"], ["society-and-economics", "political-philosophy", "history"],
      ["william-james", "hegel"],
      "Sociologist, historian and activist who named the 'double consciousness' of Black Americans.",
      "W. E. B. Du Bois studied with William James at Harvard and in Berlin, and in 1895 became the first African "
      "American to earn a Harvard PhD. His pioneering sociological study The Philadelphia Negro was followed by "
      "The Souls of Black Folk, which made him the leading intellectual voice against segregation. He co-founded "
      "the NAACP, edited its magazine The Crisis for a quarter of a century, organised Pan-African congresses, and "
      "wrote a landmark history of Reconstruction. He died in Ghana on the eve of the 1963 March on Washington."),
    T("kitaro-nishida", "Kitarō Nishida", 1870, 1945, "Kahoku, Ishikawa, Japan", "contemporary",
      ["kyoto-school"], ["metaphysics", "epistemology", "ethics"], ["william-james", "hegel", "dogen"],
      "Founder of the Kyoto School, who brought Zen into dialogue with Western philosophy.",
      "Nishida Kitarō taught high school for years while practising Zen meditation intensively, before becoming a "
      "professor at Kyoto Imperial University. His first book, An Inquiry into the Good (1911), is often called "
      "the first original work of modern Japanese philosophy. Drawing on William James's 'pure experience', German "
      "idealism and Zen, he sought a standpoint prior to the split between subject and object, later developing a "
      "'logic of place' centred on 'absolute nothingness'. The Kyoto School he founded continues to shape "
      "comparative philosophy worldwide."),
    T("bertrand-russell", "Bertrand Russell", 1872, 1970, "Trellech, Wales", "contemporary",
      ["analytic-philosophy"], ["logic", "epistemology", "political-philosophy"],
      ["leibniz", "john-stuart-mill", "david-hume"],
      "Logician, pacifist and public intellectual who helped found analytic philosophy.",
      "Bertrand Russell was the orphaned grandson of a Prime Minister and the secular godson of John Stuart Mill. "
      "With Alfred North Whitehead he wrote Principia Mathematica, an attempt to derive mathematics from logic, and "
      "his theory of descriptions became a model of analytic philosophy. Jailed for pacifist activism during the "
      "First World War, he later campaigned against nuclear weapons and was imprisoned again at 89. He wrote on "
      "marriage, education, happiness and religion with lucid wit, won the Nobel Prize in Literature in 1950, and "
      "saw his History of Western Philosophy become an unlikely bestseller."),
    T("will-durant", "Will Durant", 1885, 1981, "North Adams, Massachusetts", "contemporary", ["historiography"],
      ["history"], ["plato", "baruch-spinoza"],
      "Popular historian who brought philosophy and civilisation to millions of readers.",
      "Will Durant studied for the priesthood before turning to socialism, teaching and philosophy, earning a PhD "
      "from Columbia. The Story of Philosophy (1926), grown out of lectures and popular pamphlets, became one of "
      "the bestselling nonfiction books of its day and funded his life's project: The Story of Civilization, an "
      "eleven-volume history written with his wife, Ariel. The couple won the Pulitzer Prize in 1968 and the "
      "Presidential Medal of Freedom in 1977."),
    T("ludwig-wittgenstein", "Ludwig Wittgenstein", 1889, 1951, "Vienna", "contemporary",
      ["analytic-philosophy"], ["philosophy-of-language", "logic", "philosophy-of-mind"],
      ["bertrand-russell", "arthur-schopenhauer", "soren-kierkegaard"],
      "Viennese genius who twice transformed the philosophy of language.",
      "Ludwig Wittgenstein was born into one of the richest families in Europe, studied engineering, and arrived in "
      "Cambridge to work with Russell, who soon felt the student had surpassed him. He finished the Tractatus while "
      "serving in the Austrian army during the First World War, believed he had solved philosophy's problems, gave "
      "away his fortune and became a village schoolteacher. Returning to Cambridge in 1929, he dismantled his own "
      "earlier views: meaning is not a picture of facts but use within 'language-games' embedded in forms of life. "
      "Dying, he said: 'Tell them I've had a wonderful life.'"),
    T("martin-heidegger", "Martin Heidegger", 1889, 1976, "Meßkirch, Baden", "contemporary",
      ["phenomenology", "existentialism"], ["metaphysics", "meaning-of-life"],
      ["edmund-husserl", "aristotle", "soren-kierkegaard", "friedrich-nietzsche"],
      "Phenomenologist who asked the question of Being—and joined the Nazi party.",
      "Martin Heidegger, a sexton's son who trained for the priesthood, became Husserl's assistant and in 1927 "
      "published Being and Time, which made him the most talked-about philosopher in Germany. He argued that "
      "Western thought had forgotten the question of the meaning of Being, and analysed human existence (Dasein) "
      "as thrown into a world, absorbed in everyday concerns and facing its own death. In 1933 he joined the Nazi "
      "party and became rector of Freiburg University; his private notebooks, published from 2014, revealed "
      "antisemitic passages. His thought nonetheless deeply shaped existentialism, hermeneutics, deconstruction "
      "and environmental philosophy."),
    T("karl-popper", "Karl Popper", 1902, 1994, "Vienna", "contemporary",
      ["analytic-philosophy", "liberalism"], ["philosophy-of-science", "political-philosophy"],
      ["immanuel-kant", "david-hume", "bertrand-russell"],
      "Philosopher of falsification and defender of the open society.",
      "Karl Popper grew up in Vienna, briefly flirted with Marxism, and trained as a teacher. His Logic of "
      "Scientific Discovery (1934) argued that science advances not by proving theories but by boldly conjecturing "
      "and trying to refute them: a theory that cannot possibly be falsified is not scientific. Of Jewish descent, "
      "he left for New Zealand in 1937 and wrote The Open Society and Its Enemies there as his 'war effort'. He "
      "then taught at the London School of Economics, became a hero to reformers and dissidents, and was knighted "
      "in 1965."),
    T("viktor-frankl", "Viktor Frankl", 1905, 1997, "Vienna", "contemporary", ["existentialism"],
      ["meaning-of-life", "philosophy-of-mind"], ["friedrich-nietzsche", "soren-kierkegaard"],
      "Psychiatrist and Holocaust survivor who found meaning to be the primary human drive.",
      "Viktor Frankl was a Viennese psychiatrist already developing his ideas about meaning when, in 1942, he was "
      "deported with his family to the Theresienstadt ghetto. He survived Auschwitz and subcamps of Dachau; his "
      "wife, his parents and his brother did not. In 1946 he wrote, in a matter of days, the book that became "
      "Man's Search for Meaning. His logotherapy holds that the deepest human motivation is not pleasure or power "
      "but meaning, which can be found in work, in love, and in the attitude we take toward unavoidable "
      "suffering."),
    T("jean-paul-sartre", "Jean-Paul Sartre", 1905, 1980, "Paris", "contemporary",
      ["existentialism", "phenomenology"],
      ["meaning-of-life", "ethics", "philosophy-of-mind", "political-philosophy"],
      ["edmund-husserl", "martin-heidegger", "soren-kierkegaard", "rene-descartes", "hegel"],
      "The face of existentialism: we are condemned to be free.",
      "Jean-Paul Sartre studied at the École Normale Supérieure, where he met Simone de Beauvoir, his lifelong "
      "partner. Captured as a soldier in 1940, he spent nine months in a prison camp; back in occupied Paris he "
      "published Being and Nothingness (1943) and plays like No Exit. After the war his lectures, novels and the "
      "journal Les Temps modernes made existentialism a worldwide phenomenon. Increasingly committed to Marxism "
      "and anticolonial struggles, he refused the Nobel Prize in Literature in 1964. Tens of thousands of people "
      "followed his funeral procession through Paris."),
    T("hannah-arendt", "Hannah Arendt", 1906, 1975, "Linden, Hanover", "contemporary", ["phenomenology"],
      ["political-philosophy", "ethics", "history"], ["martin-heidegger", "immanuel-kant", "augustine"],
      "Political theorist of totalitarianism, action and the banality of evil.",
      "Hannah Arendt studied with Heidegger, Husserl and Karl Jaspers and wrote her dissertation on love in "
      "Augustine. Briefly arrested by the Gestapo in 1933, she fled Germany, was later interned in France, and "
      "reached New York in 1941. The Origins of Totalitarianism (1951) made her famous; The Human Condition "
      "(1958) recovered the dignity of political action. Reporting on the trial of Adolf Eichmann for The New "
      "Yorker, she described the 'banality of evil'—terrible deeds committed by thoughtless functionaries—setting "
      "off one of the fiercest intellectual controversies of the century."),
    T("simone-de-beauvoir", "Simone de Beauvoir", 1908, 1986, "Paris", "contemporary",
      ["existentialism", "feminism", "phenomenology"], ["ethics", "political-philosophy", "meaning-of-life"],
      ["jean-paul-sartre", "hegel", "soren-kierkegaard", "mary-wollstonecraft"],
      "Existentialist philosopher and novelist who launched modern feminism.",
      "Simone de Beauvoir placed second in the notoriously difficult agrégation in philosophy in 1929—Sartre placed "
      "first—becoming at 21 one of the youngest people ever to pass. She taught philosophy, wrote novels including "
      "The Mandarins, which won the Prix Goncourt, and edited Les Temps modernes with Sartre. The Second Sex (1949) "
      "examined how women have been made into 'the Other' through biology, history, myth and upbringing, and became "
      "a founding text of second-wave feminism. Her later works confronted ageing and death with unusual frankness."),
    T("simone-weil", "Simone Weil", 1909, 1943, "Paris", "contemporary", ["christian-philosophy"],
      ["ethics", "philosophy-of-religion", "political-philosophy"], ["plato", "immanuel-kant"],
      "Mystic, activist and philosopher of attention and affliction.",
      "Simone Weil studied under the philosopher Alain and entered the École Normale Supérieure in 1928. Driven by "
      "solidarity with the oppressed, she left teaching to work on factory assembly lines, joined an anarchist unit "
      "in the Spanish Civil War, and after a series of mystical experiences turned toward Christianity while "
      "declining baptism. In London with the Free French, she reportedly refused to eat more than the rations "
      "available in occupied France and died of tuberculosis and malnutrition at 34. Her notebooks, published "
      "posthumously, influenced Camus, T. S. Eliot and Iris Murdoch."),
    T("isaiah-berlin", "Isaiah Berlin", 1909, 1997, "Riga", "contemporary",
      ["liberalism", "analytic-philosophy"], ["political-philosophy", "history"],
      ["john-stuart-mill", "immanuel-kant"],
      "Historian of ideas and defender of liberal pluralism.",
      "Isaiah Berlin was born in Riga, witnessed the Russian Revolution as a boy in Petrograd, and moved to England "
      "with his family in 1921. A dazzling Oxford conversationalist, he served in British diplomatic posts in "
      "Washington and Moscow during and after the Second World War, meeting the poet Anna Akhmatova in Leningrad. "
      "His essays—on liberty, on the Enlightenment and its enemies, on Tolstoy and Herzen—argued that human values "
      "are many and can genuinely conflict, so that any utopia promising to reconcile them all becomes a licence "
      "for tyranny. He was the founding president of Wolfson College, Oxford."),
    T("albert-camus", "Albert Camus", 1913, 1960, "Mondovi, French Algeria", "contemporary", ["existentialism"],
      ["meaning-of-life", "ethics", "political-philosophy"],
      ["friedrich-nietzsche", "soren-kierkegaard", "fyodor-dostoevsky", "blaise-pascal"],
      "Algerian-born writer who faced the absurd and chose revolt.",
      "Albert Camus grew up in poverty in Algiers; his father was killed in the First World War and his mother, "
      "partially deaf, could not read. Tuberculosis ended his hopes of an academic career, and he turned to "
      "journalism and theatre. During the Occupation he edited the Resistance newspaper Combat. His novel The "
      "Stranger and essay The Myth of Sisyphus explore the 'absurd'—the clash between our longing for meaning and "
      "the world's silence. He won the Nobel Prize in Literature in 1957 and died in a car crash three years later, "
      "an unused train ticket in his pocket."),
    T("iris-murdoch", "Iris Murdoch", 1919, 1999, "Dublin", "contemporary",
      ["analytic-philosophy", "platonism"], ["ethics", "aesthetics"],
      ["plato", "simone-weil", "jean-paul-sartre"],
      "Novelist-philosopher who restored the idea of the Good to moral philosophy.",
      "Born in Dublin and raised in London, Iris Murdoch worked with the United Nations Relief and Rehabilitation "
      "Administration in postwar Europe, wrote the first book on Sartre in English, and taught philosophy at "
      "Oxford. She then devoted herself to writing 26 novels, including the Booker Prize-winning The Sea, the Sea. "
      "In philosophy she pushed back against the dry, choice-centred ethics of her time, arguing—with Plato and "
      "Simone Weil—that morality is mostly a matter of attention: the patient, loving effort to see other people "
      "and the world justly."),
    T("john-rawls", "John Rawls", 1921, 2002, "Baltimore", "contemporary",
      ["liberalism", "analytic-philosophy", "social-contract"], ["political-philosophy", "ethics"],
      ["immanuel-kant", "john-locke", "jean-jacques-rousseau", "john-stuart-mill"],
      "Harvard philosopher who revived political philosophy with 'justice as fairness'.",
      "John Rawls lost two younger brothers to illnesses they caught from him as a child, an experience some "
      "biographers link to his lifelong concern with undeserved fortune. He served as an infantryman in the "
      "Pacific, saw the ruins of Hiroshima, and spent most of his career at Harvard. A Theory of Justice (1971) "
      "asked what principles people would choose behind a 'veil of ignorance' that hid their own place in society, "
      "and argued for equal basic liberties and for inequalities only when they benefit the least advantaged. It "
      "reshaped political philosophy."),
    T("thomas-kuhn", "Thomas Kuhn", 1922, 1996, "Cincinnati, Ohio", "contemporary", ["analytic-philosophy"],
      ["philosophy-of-science", "history"], ["karl-popper"],
      "Physicist-turned-historian who coined the 'paradigm shift'.",
      "Thomas Kuhn trained as a physicist at Harvard, but teaching the history of science convinced him that "
      "textbooks badly misrepresent how science actually develops. In The Structure of Scientific Revolutions "
      "(1962) he argued that normal science works within a 'paradigm'—a shared framework of theory, methods and "
      "exemplary problems—until accumulating anomalies trigger a crisis and a revolution. His phrase 'paradigm "
      "shift' escaped into everyday language, and the book became one of the most cited academic works of the "
      "twentieth century."),
    T("frantz-fanon", "Frantz Fanon", 1925, 1961, "Fort-de-France, Martinique", "contemporary",
      ["anticolonial-thought", "existentialism"],
      ["political-philosophy", "philosophy-of-mind", "society-and-economics"],
      ["jean-paul-sartre", "hegel", "karl-marx"],
      "Psychiatrist and revolutionary who analysed the psychology of colonialism.",
      "Frantz Fanon grew up in Martinique, was taught by the poet Aimé Césaire, and fought with the Free French in "
      "the Second World War. Trained as a psychiatrist in Lyon, he published Black Skin, White Masks (1952), a "
      "searing study of how racism shapes consciousness. Posted to a psychiatric hospital in Algeria, he joined the "
      "Algerian independence struggle and became a spokesman for the National Liberation Front. He wrote The "
      "Wretched of the Earth while dying of leukaemia at 36; Sartre wrote its preface."),
    T("michel-foucault", "Michel Foucault", 1926, 1984, "Poitiers", "contemporary", ["post-structuralism"],
      ["political-philosophy", "history", "society-and-economics", "epistemology"],
      ["friedrich-nietzsche", "martin-heidegger", "immanuel-kant"],
      "Historian of madness, prisons and sexuality who rethought power.",
      "Michel Foucault was a troubled student at the École Normale Supérieure who went on to hold a chair at the "
      "Collège de France in the 'History of Systems of Thought'. His books trace how institutions and forms of "
      "knowledge—psychiatry, medicine, criminology, sexology—define what counts as normal and shape who we are. "
      "Power, he argued, is not only repression from above but a productive network running through everyday "
      "practices of surveillance, examination and discipline. An activist for prisoners' rights, he died of an "
      "AIDS-related illness in 1984 and remains one of the most cited scholars in the humanities."),
    T("jared-diamond", "Jared Diamond", 1937, None, "Boston", "contemporary", ["historiography"],
      ["history", "society-and-economics"], [],
      "Geographer and biologist who asked why history unfolded differently on different continents.",
      "Jared Diamond trained as a physiologist, studied the birds of New Guinea for decades, and later became a "
      "professor of geography at UCLA. A question from a New Guinean politician named Yali—why did white people "
      "have so much 'cargo' and his people so little?—launched Guns, Germs, and Steel (1997), which won the "
      "Pulitzer Prize. He has gone on to write about the collapse of societies, traditional ways of life and "
      "national crises, always looking for environmental and geographic causes beneath the course of history."),
    T("thomas-nagel", "Thomas Nagel", 1937, None, "Belgrade", "contemporary", ["analytic-philosophy"],
      ["philosophy-of-mind", "ethics", "meaning-of-life"], ["john-rawls", "ludwig-wittgenstein"],
      "Philosopher of mind who asked what it is like to be a bat.",
      "Thomas Nagel was born in Belgrade to German-Jewish refugee parents and grew up in the United States. "
      "Educated at Cornell, Oxford and Harvard, where he studied with John Rawls, he taught for decades at New York "
      "University. His 1974 essay 'What Is It Like to Be a Bat?' argued that physical science, however complete, "
      "leaves out the subjective character of experience—a central text in the debate over consciousness. His work "
      "on the tension between subjective and objective viewpoints spans ethics, politics, the absurd and the "
      "meaning of life."),
    T("robert-nozick", "Robert Nozick", 1938, 2002, "Brooklyn, New York", "contemporary",
      ["analytic-philosophy", "liberalism"], ["political-philosophy", "epistemology", "meaning-of-life"],
      ["john-locke", "john-rawls", "immanuel-kant"],
      "Harvard philosopher who made the case for the minimal state.",
      "Robert Nozick was a Harvard colleague of John Rawls whose Anarchy, State, and Utopia (1974) mounted the "
      "most famous libertarian reply to A Theory of Justice and won a National Book Award. He refused to stay in "
      "one corner of philosophy, writing on free will, personal identity, knowledge, rationality and the meaning "
      "of life, and proposed the famous 'experience machine' thought experiment. Later in life he distanced "
      "himself from some of his earlier libertarian conclusions."),
    T("peter-singer", "Peter Singer", 1946, None, "Melbourne", "contemporary",
      ["utilitarianism", "analytic-philosophy"], ["ethics"], ["john-stuart-mill"],
      "Utilitarian ethicist behind animal liberation and effective altruism.",
      "Peter Singer's parents fled Nazi-occupied Vienna for Australia; most of his grandparents were killed in the "
      "Holocaust. While a graduate student at Oxford he became convinced that the way humans treat animals is "
      "indefensible, and Animal Liberation (1975) helped launch the modern animal rights movement. His essay "
      "'Famine, Affluence, and Morality' argued that if we can prevent something very bad without sacrificing "
      "anything of comparable moral importance, we ought to do it—an idea that inspired the effective altruism "
      "movement. Long based at Princeton, he is among the most influential and most debated living philosophers."),
    T("jostein-gaarder", "Jostein Gaarder", 1952, None, "Oslo", "contemporary", [],
      ["meaning-of-life", "history"], [],
      "Norwegian teacher whose novel made the history of philosophy a bestseller.",
      "Jostein Gaarder taught philosophy at a secondary school in Bergen before becoming a full-time writer. "
      "Sophie's World (1991), a novel in which a teenage girl receives mysterious letters guiding her through the "
      "history of Western philosophy, became an international phenomenon, translated into some sixty languages and "
      "selling tens of millions of copies. For many readers around the world it was their first introduction to "
      "Socrates, Descartes and Kant."),
    T("yuval-noah-harari", "Yuval Noah Harari", 1976, None, "Kiryat Ata, Israel", "contemporary",
      ["historiography"], ["history", "society-and-economics", "meaning-of-life"], ["jared-diamond"],
      "Israeli historian whose 'brief history of humankind' became a global phenomenon.",
      "Yuval Noah Harari earned his doctorate at Oxford as a specialist in medieval military history and teaches at "
      "the Hebrew University of Jerusalem. An introductory course on world history he taught there became Sapiens: "
      "A Brief History of Humankind, first published in Hebrew in 2011, which has since sold many millions of "
      "copies worldwide. Its central argument—that humans came to dominate the planet thanks to our unique ability "
      "to believe in shared fictions such as gods, nations and money—has made him one of the most widely read "
      "public intellectuals of the century."),
]
