"""Eras, schools and topics: the scaffolding of the catalogue."""

ERAS = [
    dict(
        slug="ancient",
        name="Antiquity",
        start=-800,
        end=500,
        color="#c0703f",
        summary="From the first Greek, Indian and Chinese sages to the fall of Rome.",
        description=(
            "Around the sixth century BCE, in Greece, India and China, people began to ask questions in a new way: "
            "not 'what do the gods want?' but 'what is everything made of?', 'how should I live?' and 'what makes "
            "a ruler legitimate?'. The answers given by Confucius and Laozi, the Buddha, Socrates, Plato and "
            "Aristotle, and later by the Stoics and Epicureans, still frame how billions of people think. "
            "Historians like Herodotus and Thucydides invented the critical study of the past."
        ),
    ),
    dict(
        slug="medieval",
        name="Middle Ages",
        start=500,
        end=1450,
        color="#8a6bc2",
        summary="Faith and reason in dialogue across the Christian, Islamic, Jewish and Buddhist worlds.",
        description=(
            "Far from a 'dark age', the medieval millennium saw philosophy flourish in Baghdad, Córdoba, Cairo, "
            "Paris, Oxford and Kyoto. Thinkers such as Avicenna, al-Ghazali, Averroes, Maimonides and Aquinas "
            "wrestled with how revealed religion fits with the philosophy of Aristotle and Plato, producing "
            "sophisticated theories of logic, language, mind and God. Ibn Khaldun founded a science of history "
            "and society."
        ),
    ),
    dict(
        slug="renaissance",
        name="Renaissance",
        start=1450,
        end=1600,
        color="#3f9c78",
        summary="Humanists rediscover the classics, and the printing press spreads new ideas fast.",
        description=(
            "Printing, the recovery of Greek texts, voyages of exploration and the Reformation shook old certainties. "
            "Humanists like Erasmus and More turned scholarship toward ethics and reform; Machiavelli looked at "
            "power without illusions; Montaigne invented the essay; and in China Wang Yangming taught the unity "
            "of knowledge and action."
        ),
    ),
    dict(
        slug="early-modern",
        name="Early Modern & Enlightenment",
        start=1600,
        end=1800,
        color="#4a86c5",
        summary="The scientific revolution, the social contract and the Age of Reason.",
        description=(
            "Inspired by the new science, Descartes, Spinoza, Locke, Hume and Kant asked what we can really know and "
            "rebuilt philosophy on new foundations. Hobbes, Locke and Rousseau explained government as a contract "
            "among free people, ideas that fuelled the American and French revolutions. Voltaire, Smith, "
            "Wollstonecraft and Gibbon made the Enlightenment a project of reason, tolerance and reform."
        ),
    ),
    dict(
        slug="modern",
        name="Nineteenth Century",
        start=1800,
        end=1900,
        color="#c4485a",
        summary="Revolutions, industry and the death of God.",
        description=(
            "Hegel saw history as the march of freedom; Marx turned that vision toward economics and class struggle. "
            "Mill defended liberty and equality, Kierkegaard and Nietzsche confronted faith and nihilism, and "
            "Emerson and Thoreau sought wisdom in nature and self-reliance. Tocqueville explained democracy, and "
            "Dostoevsky turned philosophical arguments into novels."
        ),
    ),
    dict(
        slug="contemporary",
        name="Twentieth Century & Today",
        start=1900,
        end=None,
        color="#d1a23a",
        summary="Language, existence, justice and the history of everything.",
        description=(
            "Analytic philosophers like Russell and Wittgenstein turned to logic and language, while phenomenologists "
            "and existentialists like Heidegger, Sartre, Beauvoir and Camus explored lived experience, freedom and "
            "the absurd. After two world wars, Arendt, Popper, Fanon, Rawls and Foucault rethought power, justice "
            "and liberation, and a new generation of historians told the story of humanity as a whole."
        ),
    ),
]

SCHOOLS = [
    ("presocratics", "Presocratic Philosophy", "ancient",
     "The first Greek philosophers, who sought the underlying nature of the cosmos through reason rather than myth."),
    ("platonism", "Platonism", "ancient",
     "The tradition of Plato: true reality lies in eternal, intelligible Forms, and the soul's task is to know them."),
    ("aristotelianism", "Aristotelianism", "ancient",
     "Aristotle's tradition of logic, empirical inquiry and virtue ethics, dominant in medieval universities."),
    ("stoicism", "Stoicism", "ancient",
     "Live according to nature and reason; distinguish what is up to you from what is not; virtue is the only good."),
    ("epicureanism", "Epicureanism", "ancient",
     "The world is atoms and void; the good life is tranquil pleasure, friendship and freedom from fear."),
    ("skepticism", "Skepticism", "ancient",
     "Suspend judgement where certainty is impossible—and find peace of mind in doing so."),
    ("confucianism", "Confucianism", "ancient",
     "Self-cultivation, humaneness, ritual and learning as the basis of family, society and government."),
    ("taoism", "Taoism", "ancient",
     "Harmony with the Tao, the nameless Way of nature, through simplicity, spontaneity and effortless action."),
    ("buddhism", "Buddhist Philosophy", "ancient",
     "Analysis of suffering, impermanence and the self, and a path of ethics, meditation and wisdom to liberation."),
    ("neoplatonism", "Neoplatonism", "ancient",
     "Plotinus' vision of reality flowing from the One, and the soul's return to it through contemplation."),
    ("historiography", "History & Historiography", "ancient",
     "The great historians, from Herodotus to today, and the craft of explaining why things happened."),
    ("political-realism", "Political Realism", "ancient",
     "Politics as it is, not as it ought to be: power, fear and interest drive states and rulers."),
    ("christian-philosophy", "Christian Philosophy", "ancient",
     "Thinkers who brought philosophical reason to bear on Christian faith, from Augustine to Kierkegaard and Weil."),
    ("islamic-philosophy", "Islamic Philosophy", "medieval",
     "The falsafa tradition of the Islamic world, which developed Greek philosophy and transmitted it to Europe."),
    ("jewish-philosophy", "Jewish Philosophy", "medieval",
     "Reflection on reason, revelation and Jewish law, above all in the work of Maimonides."),
    ("scholasticism", "Scholasticism", "medieval",
     "The rigorous method of the medieval universities, reconciling Christian theology with Aristotle."),
    ("renaissance-humanism", "Renaissance Humanism", "renaissance",
     "A return to classical sources, eloquence and human dignity as the basis of education and reform."),
    ("neo-confucianism", "Neo-Confucianism", "renaissance",
     "Renewed Confucian thought that absorbed Buddhist and Taoist metaphysics into a philosophy of the moral mind."),
    ("rationalism", "Rationalism", "early-modern",
     "Reason, not the senses, is the chief source of knowledge; the world has a rational structure."),
    ("empiricism", "Empiricism", "early-modern",
     "All knowledge comes from experience; claims must be tested against observation."),
    ("social-contract", "Social Contract Theory", "early-modern",
     "Political authority is legitimate because free individuals agree, or would agree, to it."),
    ("enlightenment", "The Enlightenment", "early-modern",
     "The Age of Reason: tolerance, science, rights and the courage to think for yourself."),
    ("liberalism", "Liberalism", "early-modern",
     "Individual liberty, rights, constitutional government and the limits of state power."),
    ("conservatism", "Conservatism", "early-modern",
     "Respect for inherited institutions and gradual reform over revolutionary change."),
    ("feminism", "Feminist Philosophy", "early-modern",
     "Critique of the subordination of women and inquiry into how gender shapes knowledge, ethics and power."),
    ("german-idealism", "German Idealism", "modern",
     "After Kant: the mind's role in constituting reality, from Hegel's Spirit to Schopenhauer's Will."),
    ("utilitarianism", "Utilitarianism", "modern",
     "The right action is the one that produces the greatest happiness for the greatest number."),
    ("transcendentalism", "Transcendentalism", "modern",
     "American movement trusting intuition, nature and the divinity of the individual soul."),
    ("marxism", "Marxism", "modern",
     "History as class struggle; capitalism as a system of exploitation destined to be overcome."),
    ("existentialism", "Existentialism", "modern",
     "Existence precedes essence: we are free, responsible and must create meaning in an indifferent world."),
    ("pragmatism", "Pragmatism", "modern",
     "The meaning and truth of ideas lie in their practical consequences."),
    ("phenomenology", "Phenomenology", "contemporary",
     "Describe experience exactly as it is lived, before theorising about what lies behind it."),
    ("analytic-philosophy", "Analytic Philosophy", "contemporary",
     "Philosophy through logic, conceptual analysis and attention to language and science."),
    ("kyoto-school", "Kyoto School", "contemporary",
     "Japanese philosophers who brought Zen Buddhism into dialogue with Western thought."),
    ("anticolonial-thought", "Anticolonial & Black Thought", "contemporary",
     "Analyses of race, colonialism and liberation, from Du Bois to Fanon."),
    ("post-structuralism", "Post-structuralism", "contemporary",
     "Critique of fixed meanings and structures; attention to power, discourse and difference."),
]

TOPICS = [
    ("ethics", "Ethics", "How should I live, and what do I owe others?",
     "The study of right and wrong, virtue, duty and the good life."),
    ("metaphysics", "Metaphysics", "What is ultimately real?",
     "Being, substance, causation, time, God and the fundamental nature of reality."),
    ("epistemology", "Epistemology", "What can I know, and how?",
     "Knowledge, belief, evidence, skepticism and the limits of reason."),
    ("logic", "Logic", "What follows from what?",
     "The principles of valid reasoning and the structure of arguments."),
    ("political-philosophy", "Political Philosophy", "What makes power legitimate?",
     "Justice, the state, rights, liberty, equality and revolution."),
    ("aesthetics", "Aesthetics", "What is beauty, and why does art matter?",
     "Art, beauty, the sublime and taste."),
    ("philosophy-of-mind", "Philosophy of Mind", "What is a mind?",
     "Consciousness, the self, the mind–body problem and personal identity."),
    ("philosophy-of-religion", "Philosophy of Religion", "Is there a God, and what follows if there is?",
     "Faith and reason, arguments for and against God, evil and the sacred."),
    ("philosophy-of-science", "Philosophy of Science", "What makes knowledge scientific?",
     "Method, explanation, induction, falsification and scientific revolutions."),
    ("philosophy-of-language", "Philosophy of Language", "How do words mean?",
     "Meaning, reference, truth and the limits of what can be said."),
    ("meaning-of-life", "The Meaning of Life", "What makes a life worth living?",
     "Happiness, death, the absurd, freedom and how to live well."),
    ("history", "History", "What happened, and why?",
     "The great histories and the philosophy of history."),
    ("society-and-economics", "Society & Economics", "How do societies work, and how do they change?",
     "Markets, class, inequality, institutions and the forces that shape civilisations."),
]
