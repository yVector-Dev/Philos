"""Works from the seventeenth century to today."""

from .works_classical import W

WORKS_MODERN = [
    # ── Early Modern & Enlightenment ───────────────────────────────────────
    W("leviathan", "Leviathan", "thomas-hobbes", 1651, "treatise", "English", 500, 3,
      ["political-philosophy", "philosophy-of-mind"],
      "Without government, life is 'solitary, poor, nasty, brutish, and short': Hobbes' case for an absolute "
      "sovereign.",
      "Written during the English Civil War, Leviathan starts from the mechanics of human sensation and passion and "
      "arrives at politics. In a state of nature, roughly equal and fearful humans would fall into a war of all "
      "against all. Rational people would therefore agree to transfer their right of self-government to a "
      "sovereign—the great Leviathan—whose power to keep the peace must be undivided. Its famous frontispiece shows "
      "a giant crowned figure composed of countless tiny people.",
      ["In the state of nature, life is a war of all against all.",
       "People create the state by a social contract in order to escape fear.",
       "Sovereignty must be undivided to keep the peace."],
      pd=True, featured=True),
    W("discourse-on-the-method", "Discourse on the Method", "rene-descartes", 1637, "essay", "French", 80, 2,
      ["epistemology", "philosophy-of-science"],
      "Descartes' intellectual autobiography and four rules for thinking clearly—home of 'I think, therefore I am'.",
      "Published in French rather than Latin so that anyone with good sense could read it, the Discourse was "
      "originally a preface to essays on optics, meteorology and geometry. Descartes tells how he found his "
      "schooling uncertain, resolved to accept only what he clearly and distinctly knew, and devised four rules of "
      "method. In Part Four he arrives at his first certainty: 'I think, therefore I am'.",
      ["Accept nothing as true that you do not clearly and distinctly know.",
       "Divide problems into parts and proceed from the simple to the complex.",
       "I think, therefore I am."],
      original="Discours de la méthode", pd=True),
    W("meditations-on-first-philosophy", "Meditations on First Philosophy", "rene-descartes", 1641, "treatise",
      "Latin", 100, 3, ["epistemology", "metaphysics", "philosophy-of-mind"],
      "Six meditations in which Descartes doubts everything—even that he has a body—in order to rebuild knowledge.",
      "Over six 'days' of meditation, Descartes tears down his beliefs: the senses deceive, he might be dreaming, an "
      "evil demon might be fooling him even about mathematics. One thing survives: as long as he thinks, he exists. "
      "From there he argues for God's existence, the reliability of clear and distinct ideas, and a real distinction "
      "between mind and body. Published with objections from Hobbes, Gassendi and others, and Descartes' replies, "
      "it launched modern philosophy.",
      ["Radical doubt: the senses, dreams and an evil demon may all deceive us.",
       "The cogito: I am, I exist, whenever I think it.",
       "Mind and body are distinct substances."],
      original="Meditationes de prima philosophia", pd=True, featured=True),
    W("pensees", "Pensées", "blaise-pascal", 1670, "aphorisms", "French", 350, 2,
      ["philosophy-of-religion", "meaning-of-life"],
      "Fragments of an unfinished defence of Christianity—brilliant on boredom, diversion, reason and the heart.",
      "Published eight years after Pascal's death from the bundles of notes he left behind, the Pensées "
      "('Thoughts') are fragments of a planned apology for Christianity. They portray humanity as a 'thinking "
      "reed', great and wretched, suspended between infinity and nothingness and fleeing self-knowledge through "
      "diversion. They include Pascal's Wager, which argues that a rational person should bet on God. Many find "
      "them the most modern book of the seventeenth century.",
      ["We flee our condition through diversion; we cannot sit quietly in a room.",
       "The heart has its reasons which reason does not know.",
       "Pascal's Wager: weigh the infinite stakes of belief."],
      original="Pensées", pd=True, featured=True),
    W("ethics-spinoza", "Ethics", "baruch-spinoza", 1677, "treatise", "Latin", 250, 5,
      ["metaphysics", "ethics", "philosophy-of-mind", "philosophy-of-religion"],
      "Proved 'in geometrical order', Spinoza's system: God is Nature, and freedom is understanding.",
      "Laid out like Euclid, with definitions, axioms, propositions and proofs, Spinoza's Ethics moves from God to "
      "the human mind, the emotions, bondage and freedom. There is only one substance, God or Nature, of which "
      "minds and bodies are modes. Everything follows necessarily; there is no free will in the ordinary sense. Yet "
      "by understanding the causes of our passions we can transform them, attaining a calm joy he calls the "
      "intellectual love of God. Published after his death, it was condemned as atheism and later revered by "
      "Goethe, Hegel and Einstein.",
      ["There is one infinite substance: God, or Nature.",
       "Mind and body are two aspects of one reality.",
       "Freedom is understanding necessity; knowledge turns passions into active joy."],
      original="Ethica, ordine geometrico demonstrata", pd=True, featured=True),
    W("second-treatise-of-government", "Second Treatise of Government", "john-locke", 1689, "treatise",
      "English", 130, 2, ["political-philosophy"],
      "Governments exist to protect life, liberty and property—and may be resisted when they betray that trust.",
      "Published anonymously at the end of 1689, the Second Treatise argues that people in a state of nature "
      "already have natural rights, including property earned by mixing their labour with the world. They form "
      "governments by consent to secure those rights more effectively. If rulers act against that trust, the "
      "people may dissolve the government. These ideas inspired the American and French revolutions.",
      ["All people are naturally free and equal, with rights to life, liberty and property.",
       "Legitimate government rests on the consent of the governed.",
       "When government betrays its trust, the people may resist."],
      pd=True, featured=True),
    W("essay-concerning-human-understanding", "An Essay Concerning Human Understanding", "john-locke", 1689,
      "treatise", "English", 700, 4, ["epistemology", "philosophy-of-mind", "philosophy-of-language"],
      "The mind begins as a blank slate: Locke's foundational work of empiricism.",
      "Locke sets out to examine the 'original, certainty, and extent of human knowledge'. He attacks the doctrine "
      "of innate ideas and argues that all ideas come from experience—sensation and reflection. He distinguishes "
      "primary qualities (shape, motion) from secondary ones (colour, taste), offers an influential account of "
      "personal identity based on consciousness and memory, and analyses language. The Essay set the agenda for "
      "Berkeley, Hume and the Enlightenment.",
      ["There are no innate ideas; the mind starts as a blank slate.",
       "All ideas derive from sensation or reflection.",
       "Personal identity consists in continuity of consciousness."],
      pd=True),
    W("monadology", "Monadology", "leibniz", 1714, "treatise", "French", 30, 4,
      ["metaphysics"],
      "In 90 brief paragraphs, Leibniz sketches a universe of simple, mind-like substances in pre-established "
      "harmony.",
      "Written in Vienna near the end of his life, the Monadology summarises Leibniz's metaphysics. Reality "
      "consists of monads—simple, indivisible, non-spatial substances, each mirroring the whole universe from its "
      "own point of view. Monads 'have no windows': they do not causally interact, but God has synchronised them "
      "in a pre-established harmony. God, choosing among infinitely many possible worlds, created the best one.",
      ["Reality is made of simple substances—monads—each a perspective on the universe.",
       "Monads have no windows; their harmony is pre-established by God.",
       "This is the best of all possible worlds."],
      original="La Monadologie", pd=True),
    W("principles-of-human-knowledge", "A Treatise Concerning the Principles of Human Knowledge",
      "george-berkeley", 1710, "treatise", "English", 120, 3, ["metaphysics", "epistemology"],
      "Berkeley's case that physical objects are nothing but ideas—to be is to be perceived.",
      "Written when he was 25, Berkeley's Principles argues that the notion of material substance existing "
      "independently of minds is incoherent. Everything we know of a cherry—its colour, taste, softness—is a "
      "sensation in a mind; take those away and nothing is left. Reality consists of minds and their ideas, with "
      "God's mind sustaining the regular order of nature. His argument has never been easy to refute, as Samuel "
      "Johnson discovered when he kicked a stone and declared 'I refute it thus'.",
      ["To be is to be perceived (esse est percipi).",
       "The idea of unperceived matter is incoherent.",
       "The order of nature is a language of ideas spoken by God."],
      pd=True),
    W("the-spirit-of-the-laws", "The Spirit of the Laws", "montesquieu", 1748, "treatise", "French", 750, 3,
      ["political-philosophy", "society-and-economics"],
      "A sweeping comparative study of laws and governments—and the case for the separation of powers.",
      "Many years in the writing, The Spirit of the Laws argues that laws must fit a nation's climate, religion, "
      "commerce, customs and form of government. Montesquieu classifies governments as republics (driven by "
      "virtue), monarchies (honour) and despotisms (fear). Admiring England, he argues that liberty depends on "
      "separating legislative, executive and judicial power so that 'power checks power'. The American founders "
      "cited him more than almost any other modern author.",
      ["Laws must suit the character and circumstances of a people.",
       "Liberty requires the separation of legislative, executive and judicial powers.",
       "Commerce tends to soften manners and promote peace."],
      original="De l'esprit des lois", pd=True),
    W("candide", "Candide", "voltaire", 1759, "novel", "French", 130, 1,
      ["philosophy-of-religion", "ethics", "meaning-of-life"],
      "Voltaire's hilarious, savage satire of optimism: a young man's misadventures in 'the best of all possible "
      "worlds'.",
      "Expelled from a Westphalian castle for kissing the baron's daughter, the naïve Candide endures war, "
      "earthquake, shipwreck, the Inquisition and endless betrayal, while his tutor Pangloss insists that all is "
      "for the best. Written partly in response to the Lisbon earthquake of 1755, Candide mocks Leibnizian "
      "optimism, religious fanaticism and human cruelty at breakneck speed. It ends with famously understated "
      "advice: 'we must cultivate our garden'.",
      ["Glib optimism cannot survive contact with real suffering.",
       "Fanaticism and cruelty are human, not divine, works.",
       "We must cultivate our garden: modest, practical work gives life meaning."],
      original="Candide, ou l'Optimisme", pd=True, featured=True),
    W("enquiry-concerning-human-understanding", "An Enquiry Concerning Human Understanding", "david-hume", 1748,
      "treatise", "English", 160, 3, ["epistemology", "philosophy-of-religion", "philosophy-of-science"],
      "Hume's accessible masterpiece of skepticism about causation, induction and miracles.",
      "Disappointed by the reception of his Treatise, Hume recast its first book into this shorter, more elegant "
      "work. All ideas derive from impressions; reasoning about matters of fact depends on cause and effect; yet we "
      "never perceive a necessary connection, only one event regularly following another. Our expectation that the "
      "future will resemble the past is a habit, not a conclusion of reason. The section on miracles argues that "
      "testimony can hardly ever make a miracle more credible than the falsehood of the report.",
      ["We never observe necessary connection—only constant conjunction.",
       "Induction rests on custom, not reason.",
       "A wise man proportions his belief to the evidence."],
      pd=True, featured=True),
    W("treatise-of-human-nature", "A Treatise of Human Nature", "david-hume", 1739, "treatise", "English", 650, 4,
      ["epistemology", "philosophy-of-mind", "ethics"],
      "Hume's youthful, radical attempt at a science of human nature—on ideas, passions and morals.",
      "Written in his twenties, largely in France, the Treatise applies the experimental method to the mind. Book "
      "One argues that the self is nothing but a bundle of perceptions and that causal reasoning rests on habit. "
      "Book Two argues that 'reason is, and ought only to be the slave of the passions'. Book Three grounds "
      "morality in sentiment rather than reason and raises the problem of deriving 'ought' from 'is'. It is now "
      "regarded as one of the greatest works of philosophy in English.",
      ["The self is a bundle of perceptions.",
       "Reason is the slave of the passions.",
       "You cannot derive an 'ought' from an 'is'."],
      pd=True),
    W("the-social-contract", "The Social Contract", "jean-jacques-rousseau", 1762, "treatise", "French", 160, 3,
      ["political-philosophy"],
      "'Man is born free, and everywhere he is in chains.' Rousseau's theory of legitimate political community.",
      "Rousseau asks how people can unite in society while remaining as free as before. His answer is a social "
      "contract in which each gives himself wholly to the community, which is ruled by the 'general will'—the "
      "shared will for the common good, distinct from the sum of private interests. Sovereignty belongs "
      "inalienably to the people. Banned in Geneva and France on publication, it became a bible of the French "
      "Revolution and remains central to debates about democracy.",
      ["Legitimate authority comes only from a social contract among free equals.",
       "The general will aims at the common good, not private interest.",
       "Sovereignty belongs to the people and cannot be transferred."],
      original="Du contrat social", pd=True, featured=True),
    W("discourse-on-inequality", "Discourse on Inequality", "jean-jacques-rousseau", 1755, "essay", "French", 100, 2,
      ["political-philosophy", "society-and-economics"],
      "How did inequality begin? Rousseau's conjectural history blames property and society, not nature.",
      "Written for a prize competition of the Academy of Dijon (which it did not win), the Second Discourse "
      "imagines humanity in a state of nature: solitary, peaceful, moved by self-preservation and pity. Inequality "
      "arose with settled life, comparison, pride and above all private property: the first man who enclosed a "
      "piece of ground, said 'This is mine', and found people simple enough to believe him was the true founder "
      "of civil society. Its critique of civilisation shaped socialism and anthropology.",
      ["Natural humans are free, independent and compassionate.",
       "Private property and social comparison are the roots of inequality.",
       "Much of our misery is artificial, produced by society."],
      original="Discours sur l'origine et les fondements de l'inégalité parmi les hommes", pd=True),
    W("wealth-of-nations", "The Wealth of Nations", "adam-smith", 1776, "treatise", "English", 1000, 3,
      ["society-and-economics", "political-philosophy"],
      "The founding book of economics: how the division of labour and free markets create prosperity.",
      "Smith begins with a pin factory, where the division of labour multiplies productivity, and builds to a "
      "comprehensive account of markets, prices, wages, capital and trade. Individuals pursuing their own interest "
      "are led, as if by an 'invisible hand', to promote the public good. He attacks mercantilism and monopoly, "
      "warns that merchants conspire against the public, and argues for public education and public works. "
      "Published the same year as the Declaration of Independence, it shaped the modern world.",
      ["The division of labour is the engine of productivity.",
       "Self-interest in competitive markets can serve the common good.",
       "Monopolies and merchant collusion harm the public."],
      original="An Inquiry into the Nature and Causes of the Wealth of Nations", pd=True, featured=True),
    W("theory-of-moral-sentiments", "The Theory of Moral Sentiments", "adam-smith", 1759, "treatise", "English",
      400, 3, ["ethics"],
      "Before economics, Smith's theory of morality: sympathy, conscience and the impartial spectator.",
      "Smith reportedly considered this, rather than The Wealth of Nations, his better book. It opens by observing "
      "that however selfish man may be supposed, there are principles in his nature that interest him in the "
      "fortune of others. Through sympathy we imaginatively share others' feelings; through the imagined gaze of "
      "an 'impartial spectator' we learn to judge ourselves. Conscience is this inner spectator. It is a subtle "
      "portrait of humans as social, approval-seeking and capable of genuine virtue.",
      ["Sympathy—fellow-feeling—is the basis of moral judgement.",
       "Conscience is an imagined impartial spectator.",
       "We desire not only to be praised but to be genuinely praiseworthy."],
      pd=True),
    W("critique-of-pure-reason", "Critique of Pure Reason", "immanuel-kant", 1781, "treatise", "German", 800, 5,
      ["epistemology", "metaphysics"],
      "Kant's 'Copernican revolution': the mind shapes experience, and reason has limits it cannot cross.",
      "Kant set out to ask how metaphysics is possible after Hume's skepticism. His answer: objects must conform to "
      "our cognition. Space and time are forms of our intuition, and categories such as causality are concepts the "
      "understanding brings to experience. This grounds the certainty of science but limits knowledge to "
      "appearances: things in themselves remain unknowable, and when reason tries to prove God, freedom or the soul "
      "it falls into contradiction. Notoriously difficult and enormously influential, it divides philosophy into "
      "before and after.",
      ["Objects conform to the mind, not the mind to objects.",
       "Space, time and causality are conditions of any possible experience.",
       "We cannot know things in themselves; speculative metaphysics overreaches."],
      original="Kritik der reinen Vernunft", pd=True, featured=True),
    W("groundwork-of-the-metaphysics-of-morals", "Groundwork of the Metaphysics of Morals", "immanuel-kant", 1785,
      "treatise", "German", 100, 3, ["ethics"],
      "Kant's short, foundational case that morality rests on reason alone: the categorical imperative.",
      "Nothing is good without qualification except a good will, Kant begins. Actions have moral worth when done "
      "from duty, not mere inclination. The supreme principle of morality is the categorical imperative: act only "
      "on maxims you could will to become universal laws; treat humanity, in yourself and others, always as an end "
      "and never merely as a means. Brief and dense, the Groundwork is the starting point for duty-based ethics and "
      "modern ideas of human dignity.",
      ["Only a good will is good without qualification.",
       "Act only on a maxim you could will as a universal law.",
       "Treat humanity always as an end, never merely as a means."],
      original="Grundlegung zur Metaphysik der Sitten", pd=True, featured=True),
    W("what-is-enlightenment", "What Is Enlightenment?", "immanuel-kant", 1784, "essay", "German", 10, 1,
      ["political-philosophy", "epistemology"],
      "Kant's short manifesto: have the courage to use your own understanding.",
      "Answering a question posed in a Berlin journal, Kant defines enlightenment as humanity's emergence from its "
      "self-incurred immaturity—the inability to use one's understanding without another's guidance. The cause is "
      "not lack of intelligence but of courage and resolve, encouraged by guardians happy to do our thinking for "
      "us. The remedy is freedom to make public use of one's reason. In a few pages it captures the spirit of an "
      "age.",
      ["Enlightenment is emergence from self-incurred immaturity.",
       "Sapere aude: dare to think for yourself.",
       "The public use of reason must always be free."],
      original="Beantwortung der Frage: Was ist Aufklärung?", pd=True),
    W("reflections-on-the-revolution-in-france", "Reflections on the Revolution in France", "edmund-burke", 1790,
      "book", "English", 250, 3, ["political-philosophy", "history"],
      "Burke's prophetic warning that the French Revolution's abstract rights would end in tyranny.",
      "Written as a letter to a young Frenchman, Burke's Reflections attacks the Revolution's attempt to rebuild "
      "society from abstract principles. Society is a partnership between the living, the dead and those yet to be "
      "born; its inherited customs and institutions embody accumulated wisdom that no single generation can "
      "reproduce. Predicting terror and military dictatorship years before they came, it provoked replies from "
      "Paine and Wollstonecraft and founded modern conservatism.",
      ["Society is a partnership between the dead, the living and the unborn.",
       "Inherited institutions embody wisdom beyond any individual's reason.",
       "Reform cautiously; radical rupture invites tyranny."],
      pd=True),
    W("decline-and-fall-of-the-roman-empire", "The History of the Decline and Fall of the Roman Empire",
      "edward-gibbon", 1776, "history", "English", 3500, 4, ["history"],
      "Gibbon's majestic, ironic narrative of thirteen centuries, from the Antonine emperors to the fall of "
      "Constantinople.",
      "Published in six volumes between 1776 and 1789, Gibbon's history begins in the age of the Antonines, when "
      "the empire was at its height, and ends with the fall of Constantinople in 1453. Gibbon blames the decline "
      "on the loss of civic virtue, reliance on barbarian mercenaries and—controversially—the rise of "
      "Christianity. Its irony, scholarship and rolling sentences made it a literary landmark; Winston Churchill "
      "taught himself to write partly by reading it.",
      ["Rome's fall was 'the natural and inevitable effect of immoderate greatness'.",
       "The loss of civic virtue and martial spirit weakened the empire.",
       "History is largely 'the register of the crimes, follies, and misfortunes of mankind'."],
      pd=True, featured=True),
    W("common-sense", "Common Sense", "thomas-paine", 1776, "pamphlet", "English", 50, 1,
      ["political-philosophy"],
      "The pamphlet that convinced Americans to seek independence—and attacked hereditary monarchy itself.",
      "Published anonymously in January 1776, Common Sense argued in plain, forceful prose that it was absurd for "
      "an island to rule a continent, that hereditary monarchy was a fraud, and that the moment for independence "
      "had come. It sold an enormous number of copies within months and was read aloud in taverns and army camps. "
      "Its success helped make the Declaration of Independence possible six months later.",
      ["Society is a blessing; government, even at its best, a necessary evil.",
       "Hereditary monarchy is absurd and unjust.",
       "America had both the right and the interest to declare independence."],
      pd=True),
    W("vindication-of-the-rights-of-woman", "A Vindication of the Rights of Woman", "mary-wollstonecraft", 1792,
      "treatise", "English", 300, 2, ["political-philosophy", "ethics"],
      "A founding text of feminism: women are not naturally inferior, only denied education.",
      "Responding to Enlightenment thinkers—above all Rousseau—who would educate women only to please men, "
      "Wollstonecraft argues that women are rational beings who deserve the same education and moral standards as "
      "men. Raised to value beauty and sensibility above reason, women are kept in a state of dependence that "
      "degrades both them and society. Virtue requires independence. Written in about six weeks, it was both "
      "celebrated and reviled.",
      ["Women appear inferior only because they are denied education.",
       "Virtue requires reason and independence, for women as for men.",
       "Marriage should be a partnership of equals, founded on friendship."],
      pd=True, featured=True),

    # ── Nineteenth century ─────────────────────────────────────────────────
    W("phenomenology-of-spirit", "Phenomenology of Spirit", "hegel", 1807, "treatise", "German", 600, 5,
      ["metaphysics", "epistemology", "history"],
      "Hegel's odyssey of consciousness, from sense-certainty to Absolute Knowing.",
      "The Phenomenology traces the journey of consciousness through a series of shapes—sense-certainty, "
      "perception, self-consciousness, reason, spirit, religion—each collapsing under its own contradictions and "
      "giving rise to the next. Its most famous episode, the dialectic of master and slave, shows self-consciousness "
      "depending on recognition by another, and the slave, through labour, achieving a freedom the master lacks. "
      "Hard going but vastly influential, it shaped Marx, existentialism and critical theory.",
      ["The truth is the whole, reached through a process of development.",
       "Self-consciousness requires recognition by others (the master–slave dialectic).",
       "Contradictions drive thought and history forward."],
      original="Phänomenologie des Geistes"),
    W("world-as-will-and-representation", "The World as Will and Representation", "arthur-schopenhauer", 1818,
      "treatise", "German", 1000, 4, ["metaphysics", "aesthetics", "ethics", "meaning-of-life"],
      "Schopenhauer's pessimistic masterpiece: behind the world lies a blind, insatiable Will.",
      "Starting from Kant, Schopenhauer argues that the world as we perceive it is representation, shaped by our "
      "minds, but that in our own bodies we glimpse its inner essence: will—a blind, purposeless striving present "
      "in everything from gravity to sexual desire. Since willing means lack, life swings between pain and "
      "boredom. Escape comes temporarily through art, especially music, and more lastingly through compassion and "
      "the denial of the will, as taught by saints and the sages of India.",
      ["The world is representation; its inner essence is Will.",
       "Life swings like a pendulum between pain and boredom.",
       "Art, compassion and renunciation offer release from the Will."],
      original="Die Welt als Wille und Vorstellung", pd=True),
    W("self-reliance", "Self-Reliance", "ralph-waldo-emerson", 1841, "essay", "English", 30, 1,
      ["ethics", "meaning-of-life"],
      "Emerson's rousing call to trust yourself, defy conformity and live by your own light.",
      "In this essay from his first series of Essays, Emerson urges readers to stop imitating, to value their own "
      "intuitions over tradition and society, and to accept being misunderstood—'to be great is to be "
      "misunderstood'. Society, he warns, is a conspiracy against the manhood of every one of its members, and "
      "'a foolish consistency is the hobgoblin of little minds'. A key text of American individualism, it remains a "
      "perennial graduation gift.",
      ["Trust your own thought; genius is believing it is true for all.",
       "Society conspires against individuality; conformity is the enemy.",
       "A foolish consistency is the hobgoblin of little minds."],
      pd=True),
    W("democracy-in-america", "Democracy in America", "alexis-de-tocqueville", 1835, "book", "French", 900, 3,
      ["political-philosophy", "society-and-economics", "history"],
      "A young French aristocrat's brilliant analysis of American democracy, its strengths and its dangers.",
      "Published in two volumes (1835 and 1840), Tocqueville's study argues that the world is moving irresistibly "
      "toward equality of conditions, and that America shows what this will mean. He admires townships, juries, a "
      "free press and above all Americans' habit of forming voluntary associations. But he warns of the tyranny of "
      "the majority, conformity of opinion, individualism, and a 'soft despotism' in which a paternal state "
      "relieves citizens of the trouble of thinking. It remains one of the most quoted books about the United "
      "States.",
      ["Equality of conditions is the defining trend of modern history.",
       "Voluntary associations keep democratic citizens free.",
       "Beware the tyranny of the majority and soft despotism."],
      original="De la démocratie en Amérique", pd=True, featured=True),
    W("on-liberty", "On Liberty", "john-stuart-mill", 1859, "essay", "English", 120, 2,
      ["political-philosophy", "ethics"],
      "Mill's classic defence of individual freedom: the only reason to restrict liberty is to prevent harm to "
      "others.",
      "Dedicated to his late wife Harriet Taylor, On Liberty argues that the greatest threat to freedom in "
      "democratic societies is not tyrannical kings but the pressure of public opinion. Mill's 'harm principle' "
      "holds that society may interfere with individuals only to prevent harm to others. He defends free speech "
      "even for false opinions, since truth is strengthened by challenge, and praises individuality and "
      "'experiments of living'. It is a cornerstone of liberal democracy.",
      ["The harm principle: power may be exercised over individuals only to prevent harm to others.",
       "Silencing an opinion robs humanity, even if the opinion is false.",
       "Individuality and diversity are essential to human progress."],
      pd=True, featured=True),
    W("utilitarianism", "Utilitarianism", "john-stuart-mill", 1861, "essay", "English", 80, 2,
      ["ethics"],
      "Mill's defence of the greatest happiness principle—and why some pleasures are higher than others.",
      "First published as a series of articles in Fraser's Magazine, Utilitarianism defends the view that actions "
      "are right in proportion as they tend to promote happiness and wrong as they tend to produce its reverse. "
      "Answering the charge that this is a 'doctrine worthy only of swine', Mill distinguishes the higher pleasures "
      "of the intellect and feelings from lower ones. He also offers a much-debated proof of the principle and "
      "argues that justice is grounded in utility.",
      ["Actions are right insofar as they promote happiness.",
       "Some pleasures are qualitatively higher than others.",
       "Better to be Socrates dissatisfied than a fool satisfied."],
      pd=True),
    W("the-subjection-of-women", "The Subjection of Women", "john-stuart-mill", 1869, "essay", "English", 120, 2,
      ["political-philosophy", "ethics"],
      "Mill's argument for full legal and social equality between the sexes.",
      "Written with input from Harriet Taylor and his stepdaughter Helen Taylor, The Subjection of Women argues "
      "that the legal subordination of women is wrong in itself and one of the chief obstacles to human "
      "improvement. What is called 'the nature of women' is an artificial product of their circumstances. Mill "
      "demands equality in marriage, education, work and politics. Widely translated, it became a key text for "
      "suffrage movements.",
      ["The legal subordination of one sex to the other is wrong in itself.",
       "We cannot know women's 'nature' while it is shaped by oppression.",
       "Equality would double the talent available to humanity."],
      pd=True),
    W("fear-and-trembling", "Fear and Trembling", "soren-kierkegaard", 1843, "book", "Danish", 130, 3,
      ["philosophy-of-religion", "ethics", "meaning-of-life"],
      "Writing as 'Johannes de silentio', Kierkegaard confronts Abraham's willingness to sacrifice Isaac.",
      "Fear and Trembling circles obsessively around the story of Abraham, commanded by God to sacrifice his son. Is "
      "he a murderer or the father of faith? If ethics is the universal, faith seems to require a 'teleological "
      "suspension of the ethical'—a paradoxical leap no reason can justify. The pseudonymous author admires Abraham "
      "but cannot understand him. It is a disturbing meditation on faith, ethics and the limits of rational "
      "understanding.",
      ["Faith is a paradox that reason cannot mediate.",
       "The 'knight of faith' lives fully in the finite while trusting the infinite.",
       "The teleological suspension of the ethical: can faith outrank morality?"],
      original="Frygt og Bæven", featured=True),
    W("either-or", "Either/Or", "soren-kierkegaard", 1843, "book", "Danish", 600, 3,
      ["ethics", "aesthetics", "meaning-of-life"],
      "Two ways of life collide: the restless aesthete and the committed ethical man.",
      "Kierkegaard's first major work, published under the pseudonym Victor Eremita, presents papers supposedly "
      "found in a secondhand writing desk. The first volume belongs to 'A', a witty, melancholy aesthete who lives "
      "for interesting experiences and includes the notorious 'Seducer's Diary'. The second contains letters from "
      "Judge William urging A to choose himself and embrace the ethical life of commitment and marriage. The reader "
      "must decide.",
      ["The aesthetic life chases pleasure and novelty and ends in despair.",
       "The ethical life means choosing oneself through commitment.",
       "No system can make the choice for you."],
      original="Enten – Eller"),
    W("walden", "Walden", "henry-david-thoreau", 1854, "book", "English", 300, 2,
      ["meaning-of-life", "ethics"],
      "Two years in a cabin by a pond: Thoreau's experiment in living simply and deliberately.",
      "'I went to the woods because I wished to live deliberately, to front only the essential facts of life.' "
      "Walden describes Thoreau's experiment at Walden Pond near Concord, Massachusetts, compressing two years into "
      "a single cycle of seasons. Part nature writing, part economics, part spiritual autobiography, it questions "
      "the treadmill of work and acquisition and celebrates attention to the natural world. It is a founding text "
      "of environmentalism and simple living.",
      ["Most people lead lives of quiet desperation, enslaved by their wants.",
       "Simplify: a person is rich in proportion to the things they can afford to let alone.",
       "Nature is a source of wisdom and renewal."],
      original="Walden; or, Life in the Woods", pd=True, featured=True),
    W("civil-disobedience", "Civil Disobedience", "henry-david-thoreau", 1849, "essay", "English", 30, 1,
      ["political-philosophy", "ethics"],
      "Why conscience must sometimes break the law: the essay that inspired Gandhi and King.",
      "After spending a night in jail for refusing to pay a poll tax that supported slavery and the war against "
      "Mexico, Thoreau wrote this essay arguing that individuals must not let governments override their "
      "consciences: 'Under a government which imprisons any unjustly, the true place for a just man is also a "
      "prison.' Peaceful refusal to cooperate with injustice became a model for Tolstoy, Gandhi and Martin Luther "
      "King Jr.",
      ["Conscience outranks the law.",
       "Citizens must not lend themselves to the wrong they condemn.",
       "Peaceful non-cooperation can clog the machinery of injustice."],
      original="Resistance to Civil Government", pd=True),
    W("communist-manifesto", "The Communist Manifesto", "karl-marx", 1848, "pamphlet", "German", 50, 1,
      ["political-philosophy", "society-and-economics", "history"],
      "Marx and Engels' explosive pamphlet: history as class struggle, and a call for workers of the world to "
      "unite.",
      "Written by Marx and Friedrich Engels for the Communist League and published in London weeks before "
      "revolutions swept Europe in 1848, the Manifesto opens: 'A spectre is haunting Europe—the spectre of "
      "communism.' It praises the bourgeoisie for revolutionising production and sweeping away feudalism, then "
      "argues that capitalism creates its own gravediggers in the proletariat. Short, dramatic and quotable, it is "
      "one of the most influential political documents ever written.",
      ["The history of all hitherto existing society is the history of class struggles.",
       "Capitalism constantly revolutionises production: 'all that is solid melts into air'.",
       "Workers of the world, unite!"],
      original="Manifest der Kommunistischen Partei", pd=True, featured=True),
    W("capital", "Capital, Volume I", "karl-marx", 1867, "treatise", "German", 1000, 5,
      ["society-and-economics", "political-philosophy"],
      "Marx's critique of political economy: how capitalism extracts surplus value from labour.",
      "Capital begins with the humble commodity and its mysterious 'fetishism', then explains how money becomes "
      "capital by extracting surplus value: workers are paid less than the value they produce. Drawing on British "
      "factory inspectors' reports, Marx documents the working day, child labour and the machinery that displaces "
      "workers, and predicts the concentration of capital and recurring crises. Its analysis still shapes "
      "economics, sociology and history.",
      ["Commodities conceal social relations behind things (commodity fetishism).",
       "Profit comes from surplus value extracted from labour.",
       "Capitalism tends toward concentration and crisis."],
      original="Das Kapital", pd=True),
    W("notes-from-underground", "Notes from Underground", "fyodor-dostoevsky", 1864, "novel", "Russian", 130, 2,
      ["meaning-of-life", "philosophy-of-mind", "ethics"],
      "A bitter, brilliant ex-official rails against reason, progress and himself—often called the first "
      "existentialist novel.",
      "'I am a sick man... I am a spiteful man.' The unnamed narrator, a retired official living in a St "
      "Petersburg basement, attacks the rational egoism and utopian 'crystal palace' of the radicals of his day. "
      "Humans, he insists, will act against their own interests just to prove they are free and not piano keys. "
      "The second part recounts humiliating episodes from his youth. Short and corrosive, it is often seen as the "
      "gateway to existentialism.",
      ["Humans value freedom of will above rational self-interest.",
       "Too much consciousness can become a disease of endless self-scrutiny.",
       "Utopian schemes ignore human irrationality."],
      original="Записки из подполья", pd=True, featured=True),
    W("the-brothers-karamazov", "The Brothers Karamazov", "fyodor-dostoevsky", 1880, "novel", "Russian", 800, 3,
      ["philosophy-of-religion", "ethics", "meaning-of-life"],
      "A murder, three brothers and a father—and the deepest questions of faith, freedom and evil.",
      "Dostoevsky's final novel follows the passionate Dmitri, the intellectual Ivan and the gentle novice Alyosha "
      "as their debauched father is murdered. Ivan's rebellion against a God who permits the suffering of "
      "children, and his prose poem 'The Grand Inquisitor', in which Christ returns and is arrested by the "
      "Inquisition in Seville, are among the most powerful arguments in literature. Freud called it the most "
      "magnificent novel ever written.",
      ["The problem of evil: can any harmony justify the suffering of innocent children?",
       "The Grand Inquisitor: do people really want freedom—or bread and authority?",
       "Each of us is responsible for all."],
      original="Братья Карамазовы", pd=True),
    W("thus-spoke-zarathustra", "Thus Spoke Zarathustra", "friedrich-nietzsche", 1883, "book", "German", 350, 3,
      ["meaning-of-life", "ethics", "philosophy-of-religion"],
      "Nietzsche's prophetic, poetic book: the death of God, the Übermensch and eternal recurrence.",
      "Written in four parts between 1883 and 1885, Zarathustra follows a prophet who descends from his mountain "
      "to teach humanity that God is dead and that man is something to be overcome. In biblical cadences, parables "
      "and songs, he proclaims the Übermensch, the will to power, and the thought of eternal recurrence—could you "
      "will to live your life again, infinitely? Nietzsche thought it his greatest gift to humanity; readers have "
      "found it baffling, inspiring and everything in between.",
      ["God is dead; humanity must create new values.",
       "The Übermensch: overcome yourself rather than settle for comfort.",
       "Eternal recurrence: live so that you could will every moment again."],
      original="Also sprach Zarathustra", pd=True, featured=True),
    W("beyond-good-and-evil", "Beyond Good and Evil", "friedrich-nietzsche", 1886, "book", "German", 250, 3,
      ["ethics", "epistemology"],
      "Nietzsche's 'prelude to a philosophy of the future', exposing the prejudices of philosophers and moralists.",
      "In nine parts of essays and aphorisms, Nietzsche attacks the hidden assumptions of philosophers—who claim to "
      "seek truth but rationalise their instincts—and offers a natural history of morals. He distinguishes "
      "'master' from 'slave' moralities, praises 'free spirits' and perspectival thinking, and probes the will to "
      "power. Sharper and more systematic than Zarathustra, it is a good place to start.",
      ["Every great philosophy is the personal confession of its author.",
       "There are master moralities and slave moralities.",
       "All knowing is from a perspective; dogmatism mistakes one view for the whole."],
      original="Jenseits von Gut und Böse", pd=True),
    W("on-the-genealogy-of-morality", "On the Genealogy of Morality", "friedrich-nietzsche", 1887, "book", "German",
      180, 3, ["ethics"],
      "Three essays tracing our moral values to resentment, debt and the ascetic ideal.",
      "Nietzsche's most sustained argument asks where our values came from. The first essay contrasts aristocratic "
      "'good and bad' with the 'good and evil' of slave morality, born of ressentiment. The second traces guilt "
      "and bad conscience to debt and cruelty. The third asks why humanity has so often embraced the ascetic ideal "
      "of self-denial, concluding that man would rather will nothingness than not will at all. It inaugurated "
      "genealogy as a critical method, later taken up by Foucault.",
      ["Morality has a history; values are not eternal.",
       "Slave morality springs from the ressentiment of the weak against the strong.",
       "Guilt originates in debt; asceticism is a will to nothingness."],
      original="Zur Genealogie der Moral", pd=True),
    W("the-gay-science", "The Gay Science", "friedrich-nietzsche", 1882, "book", "German", 300, 3,
      ["meaning-of-life", "philosophy-of-religion", "epistemology"],
      "Nietzsche's most joyful book—home of 'God is dead' and the first statement of eternal recurrence.",
      "Written during a period of recovered health, The Gay Science (also translated as The Joyful Wisdom) "
      "celebrates a light-footed, experimental approach to knowledge and life. Section 125, in which a madman with "
      "a lantern announces in the marketplace that God is dead and that we have killed him, is one of the most "
      "famous passages in philosophy. Section 341 introduces 'the heaviest weight': a demon who tells you that you "
      "must live this life again, innumerable times.",
      ["God is dead—and we must face what this means for our values.",
       "Eternal recurrence is the ultimate test of affirming life.",
       "Knowledge should be pursued with gaiety and courage."],
      original="Die fröhliche Wissenschaft", pd=True),
    W("pragmatism", "Pragmatism", "william-james", 1907, "lectures", "English", 180, 2,
      ["epistemology", "philosophy-of-religion"],
      "James's lively lectures introducing pragmatism: truth is what works out in the long run of experience.",
      "Delivered in Boston and New York in 1906–07, these lectures present pragmatism as 'a new name for some old "
      "ways of thinking'. James offers a method for settling interminable metaphysical disputes: ask what "
      "practical difference it would make if one side or the other were true. True ideas are those we can "
      "assimilate, validate and verify; truth 'happens to an idea'. Witty and humane, it remains the best "
      "introduction to America's homegrown philosophy.",
      ["The meaning of an idea lies in its practical consequences.",
       "Truth happens to an idea: it is made true by events.",
       "Philosophy should mediate between tough-minded and tender-minded temperaments."],
      original="Pragmatism: A New Name for Some Old Ways of Thinking", pd=True),
    W("varieties-of-religious-experience", "The Varieties of Religious Experience", "william-james", 1902,
      "lectures", "English", 500, 3, ["philosophy-of-religion", "philosophy-of-mind"],
      "James studies religion from the inside: conversion, mysticism, saintliness and the 'sick soul'.",
      "Given as the Gifford Lectures in Edinburgh in 1901–02, Varieties examines religion not as institution or "
      "theology but as individual experience. Drawing on many first-person accounts, James contrasts "
      "'healthy-minded' and 'sick' souls, analyses conversion and mystical states, and asks what such experiences "
      "are worth. His pragmatic verdict: judge them by their fruits. It is a founding text of the psychology of "
      "religion.",
      ["Religion is best studied through individual experience.",
       "Mystical states are ineffable, noetic, transient and passive.",
       "Judge religious experience by its fruits for life."],
      original="The Varieties of Religious Experience: A Study in Human Nature", pd=True),

    # ── Twentieth century & today ──────────────────────────────────────────
    W("the-souls-of-black-folk", "The Souls of Black Folk", "web-du-bois", 1903, "essay", "English", 220, 2,
      ["society-and-economics", "history", "political-philosophy"],
      "Du Bois's classic essays on 'double consciousness' and the colour line in America.",
      "Combining history, sociology, autobiography and fiction, these essays trace Black American life from "
      "emancipation and Reconstruction to the Jim Crow South. Du Bois introduces 'double consciousness'—the sense "
      "of always looking at one's self through the eyes of others—and the 'veil' that separates Black and white "
      "America. He challenges Booker T. Washington's accommodationism and celebrates the 'sorrow songs' as "
      "America's great music.",
      ["The problem of the twentieth century is the problem of the colour line.",
       "Double consciousness: seeing oneself through the eyes of a contemptuous world.",
       "Higher education and civil rights, not accommodation, are the path forward."],
      pd=True, featured=True),
    W("an-inquiry-into-the-good", "An Inquiry into the Good", "kitaro-nishida", 1911, "book", "Japanese", 200, 4,
      ["metaphysics", "ethics", "epistemology"],
      "The first major work of modern Japanese philosophy, grounding reality in 'pure experience'.",
      "Nishida's first book begins with 'pure experience'—experience before it is divided into subject and "
      "object, as when we are wholly absorbed in music. From this he develops an account of reality, the good and "
      "religion: the good is the realisation of the self in unity with reality, and God is the ground of that "
      "unity. Blending William James, German idealism and Zen practice, it opened a new path in world philosophy.",
      ["Pure experience precedes the split between subject and object.",
       "The good is the self's realisation in unity with reality.",
       "Religion is the culmination of knowledge and ethics."],
      original="善の研究 (Zen no kenkyū)"),
    W("the-problems-of-philosophy", "The Problems of Philosophy", "bertrand-russell", 1912, "book", "English", 120,
      1, ["epistemology", "metaphysics"],
      "Russell's short, crystal-clear introduction to the big questions of knowledge and reality.",
      "Written for a popular series of inexpensive books, The Problems of Philosophy opens by asking whether there "
      "is any knowledge so certain that no reasonable person could doubt it. Russell covers appearance and "
      "reality, idealism, knowledge by acquaintance and by description, induction, a priori knowledge and "
      "universals. Its final chapter on the value of philosophy—which lies in its very uncertainty and in the "
      "enlargement of the self—is one of the finest defences of the subject.",
      ["Appearance and reality can come apart; even an ordinary table is puzzling.",
       "Knowledge by acquaintance differs from knowledge by description.",
       "Philosophy's value lies in its questions, which enlarge the mind."],
      pd=True, featured=True),
    W("a-history-of-western-philosophy", "A History of Western Philosophy", "bertrand-russell", 1945, "book",
      "English", 900, 2, ["history", "metaphysics", "ethics"],
      "Russell's opinionated, witty tour from the Presocratics to his own day, set against the history of society.",
      "Written largely from lectures given in the United States during the Second World War, Russell's History "
      "connects philosophers to the social and political circumstances that shaped them. It is unapologetically "
      "partisan—generous to the empiricists, caustic about Hegel and Nietzsche—but also lucid, funny and full of "
      "insight. It became a bestseller and, Russell said, his main source of income for the rest of his life.",
      ["Philosophy is part of the life of society, not separate from it.",
       "The history of thought swings between social cohesion and individual liberty.",
       "Clarity and skepticism are the philosopher's virtues."]),
    W("the-story-of-philosophy", "The Story of Philosophy", "will-durant", 1926, "book", "English", 600, 1,
      ["history"],
      "Durant's beloved, readable lives and ideas of the great philosophers, from Plato to Dewey.",
      "Durant set out to 'humanize knowledge' by centring the story of philosophy on great personalities: Plato, "
      "Aristotle, Bacon, Spinoza, Voltaire, Kant, Schopenhauer, Spencer, Nietzsche and a handful of modern "
      "Europeans and Americans. Warm, enthusiastic and sometimes opinionated, it became a runaway bestseller and "
      "introduced generations of readers to philosophy.",
      ["Philosophy is best understood through the lives of philosophers.",
       "Knowledge should be humanised and made accessible.",
       "The great questions remain living questions."]),
    W("tractatus-logico-philosophicus", "Tractatus Logico-Philosophicus", "ludwig-wittgenstein", 1921, "treatise",
      "German", 90, 5, ["philosophy-of-language", "logic", "metaphysics"],
      "A short book of numbered propositions on logic, language and the limits of what can be said.",
      "Composed during the First World War and finished in an Italian prisoner-of-war camp, the Tractatus consists "
      "of numbered remarks beginning 'The world is everything that is the case'. Language pictures possible facts; "
      "logic shows the structure that language and world share. Ethics, aesthetics and the meaning of life cannot "
      "be said, only shown—hence the closing line: 'Whereof one cannot speak, thereof one must be silent.' It "
      "inspired the Vienna Circle, who largely ignored its mystical side.",
      ["The world is the totality of facts, not of things.",
       "Propositions are pictures of possible states of affairs.",
       "What cannot be said must be passed over in silence."],
      original="Logisch-philosophische Abhandlung", pd=True),
    W("philosophical-investigations", "Philosophical Investigations", "ludwig-wittgenstein", 1953, "book", "German",
      250, 4, ["philosophy-of-language", "philosophy-of-mind"],
      "Published after his death, Wittgenstein's radical rethinking: meaning is use, and philosophy is therapy.",
      "The later Wittgenstein rejects the Tractatus picture of language as a mirror of the world. Words are tools; "
      "their meaning lies in their use within 'language-games' woven into 'forms of life'. Concepts like 'game' "
      "share no single essence, only 'family resemblances'. His private language argument suggests that talk of "
      "inner experience depends on public criteria. Philosophical problems arise 'when language goes on holiday'; "
      "the task is to show the fly the way out of the fly-bottle.",
      ["The meaning of a word is its use in the language.",
       "Concepts are held together by family resemblances, not essences.",
       "Philosophy is therapy for confusions created by language."],
      original="Philosophische Untersuchungen", featured=True),
    W("being-and-time", "Being and Time", "martin-heidegger", 1927, "treatise", "German", 500, 5,
      ["metaphysics", "meaning-of-life"],
      "Heidegger's analysis of human existence as being-in-the-world, care and being-toward-death.",
      "Heidegger sets out to reawaken the forgotten question of the meaning of Being, approaching it through the "
      "one being for whom its own being is an issue: Dasein, the human. We are not detached subjects observing "
      "objects but are 'thrown' into a world of practical involvements, usually absorbed in the anonymous 'they'. "
      "Anxiety and the anticipation of our own death can call us back to authentic existence. Unfinished and "
      "forbiddingly difficult, it reshaped twentieth-century thought.",
      ["Human existence (Dasein) is being-in-the-world, not a mind facing objects.",
       "We are thrown into situations we did not choose and usually lose ourselves in the 'they'.",
       "Facing our being-toward-death makes authentic existence possible."],
      original="Sein und Zeit"),
    W("cartesian-meditations", "Cartesian Meditations", "edmund-husserl", 1931, "lectures", "French", 160, 5,
      ["epistemology", "philosophy-of-mind"],
      "Husserl's compact introduction to phenomenology, reworking Descartes' quest for a certain foundation.",
      "Based on lectures delivered at the Sorbonne in 1929 and first published in French, the Cartesian Meditations "
      "present phenomenology as the fulfilment of Descartes' project. Through the 'epoché' we bracket our natural "
      "belief in the world and attend to how it appears in consciousness, discovering that consciousness is always "
      "consciousness of something. The fifth meditation tackles how we experience other minds—the problem of "
      "intersubjectivity.",
      ["Bracket the natural attitude (epoché) to study experience as it is given.",
       "Consciousness is always intentional: consciousness of something.",
       "Other minds are given to us through empathy and intersubjectivity."],
      original="Méditations cartésiennes"),
    W("the-open-society-and-its-enemies", "The Open Society and Its Enemies", "karl-popper", 1945, "book",
      "English", 750, 3, ["political-philosophy", "history"],
      "Popper's wartime attack on Plato, Hegel and Marx as enemies of an open, self-correcting society.",
      "Written in New Zealand during the Second World War, Popper's two volumes argue that totalitarianism draws "
      "on a long tradition of 'historicism'—the belief that history follows inexorable laws—and of utopian "
      "planning. Plato's ideal state, Hegel's philosophy of history and Marx's prophecies are his targets. Against "
      "them he defends the open society, whose institutions let citizens remove bad rulers without bloodshed and "
      "whose policies proceed by piecemeal, testable reform.",
      ["Historicism—belief in inevitable historical laws—is false and dangerous.",
       "The key question is not 'who should rule?' but how to remove bad rulers peacefully.",
       "The paradox of tolerance: unlimited tolerance leads to the disappearance of tolerance."]),
    W("the-logic-of-scientific-discovery", "The Logic of Scientific Discovery", "karl-popper", 1934, "treatise",
      "German", 500, 4, ["philosophy-of-science", "epistemology"],
      "Science advances by conjecture and refutation: Popper's case for falsifiability.",
      "Popper rejects the idea that science proves theories through accumulated observations—no number of white "
      "swans proves that all swans are white. Instead, scientists propose bold conjectures and subject them to "
      "severe tests; a theory is scientific only if it could in principle be falsified. This criterion separates "
      "science from pseudoscience. First published in German in 1934, it appeared in an expanded English edition "
      "in 1959.",
      ["Theories can never be verified, only corroborated or falsified.",
       "Falsifiability marks the boundary of science.",
       "Knowledge grows through bold conjectures and attempted refutations."],
      original="Logik der Forschung"),
    W("the-origins-of-totalitarianism", "The Origins of Totalitarianism", "hannah-arendt", 1951, "book", "English",
      600, 4, ["political-philosophy", "history"],
      "Arendt's study of antisemitism, imperialism and the unprecedented horror of Nazi and Stalinist rule.",
      "Arendt traces the elements that crystallised into totalitarianism: modern antisemitism, the imperialist "
      "politics of expansion and race, the decline of the nation-state and the creation of masses of stateless "
      "people with no 'right to have rights'. Totalitarianism, she argues, is something new: rule by ideology and "
      "terror that seeks to make human beings superfluous, culminating in the camps. It remains essential reading "
      "on how political orders collapse.",
      ["Totalitarianism is a novel form of rule by ideology and terror.",
       "Statelessness reveals that rights depend on belonging to a political community.",
       "Loneliness and atomisation prepare the ground for mass movements."]),
    W("the-human-condition", "The Human Condition", "hannah-arendt", 1958, "book", "English", 350, 4,
      ["political-philosophy", "meaning-of-life"],
      "Labour, work and action: Arendt's reflection on what we are doing when we live together.",
      "Arendt distinguishes three fundamental activities: labour, which sustains biological life; work, which "
      "builds a durable world of things; and action, through which unique individuals appear to one another in "
      "speech and deed and begin something new. Modern society, she argues, has elevated labour and consumption "
      "while losing the public space for action. Her idea of 'natality'—the capacity to begin—offers a "
      "counterweight to philosophy's long preoccupation with death.",
      ["Human activity divides into labour, work and action.",
       "Action and speech reveal who we are, and need a public space.",
       "Natality: every birth brings the capacity for new beginnings."]),
    W("eichmann-in-jerusalem", "Eichmann in Jerusalem", "hannah-arendt", 1963, "book", "English", 300, 2,
      ["ethics", "history", "political-philosophy"],
      "Arendt's report on the trial of Adolf Eichmann, and her controversial idea of the 'banality of evil'.",
      "Covering the 1961 trial in Jerusalem for The New Yorker, Arendt expected a monster and found a careerist "
      "bureaucrat who spoke in clichés and seemed incapable of thinking from anyone else's standpoint. The book's "
      "subtitle, A Report on the Banality of Evil, captured her conclusion that enormous crimes can be committed by "
      "people who simply fail to think. Her criticism of the wartime Jewish Councils provoked a fierce controversy "
      "that has never fully subsided.",
      ["Great evil can be committed by thoughtless, ordinary people.",
       "Thoughtlessness—the failure to judge from others' standpoint—enables atrocity.",
       "Obedience is no excuse for participating in crime."],
      original="Eichmann in Jerusalem: A Report on the Banality of Evil", featured=True),
    W("being-and-nothingness", "Being and Nothingness", "jean-paul-sartre", 1943, "treatise", "French", 700, 5,
      ["metaphysics", "philosophy-of-mind", "meaning-of-life"],
      "Sartre's phenomenological treatise on consciousness, freedom, bad faith and the look of the Other.",
      "Written during the Occupation, Being and Nothingness distinguishes the inert being of things "
      "('being-in-itself') from consciousness ('being-for-itself'), which is a kind of nothingness, always beyond "
      "what it is. Because we are not fixed things, we are radically free—and anxious about it. We flee into 'bad "
      "faith', like the café waiter who plays at being a waiter. Under the gaze of the Other we experience shame "
      "and objectification. Massive and dense, it is existentialism's theoretical core.",
      ["Consciousness is a nothingness that makes us radically free.",
       "Bad faith is the self-deception of pretending we are not free.",
       "The look of the Other turns us into objects."],
      original="L'Être et le néant"),
    W("existentialism-is-a-humanism", "Existentialism Is a Humanism", "jean-paul-sartre", 1946, "lectures",
      "French", 60, 1, ["ethics", "meaning-of-life"],
      "Sartre's famous lecture: existence precedes essence, and we are condemned to be free.",
      "Delivered to a packed Parisian hall in October 1945 and published the following year, this lecture defended "
      "existentialism against charges of pessimism and moral nihilism. Because there is no God to define human "
      "nature, 'existence precedes essence': we first exist, then define ourselves by our actions. We are therefore "
      "wholly responsible—and in choosing for ourselves, we choose an image of humanity for all. His example of a "
      "student torn between caring for his mother and joining the Free French is a classic of moral philosophy.",
      ["Existence precedes essence: we make ourselves through our choices.",
       "We are condemned to be free, and wholly responsible.",
       "In choosing for ourselves, we choose for all humanity."],
      original="L'existentialisme est un humanisme", featured=True),
    W("mans-search-for-meaning", "Man's Search for Meaning", "viktor-frankl", 1946, "book", "German", 160, 1,
      ["meaning-of-life", "philosophy-of-mind"],
      "A psychiatrist's account of surviving the Nazi camps, and his discovery that meaning makes life bearable.",
      "In the first part, Frankl describes life in the concentration camps with unsparing restraint: the shock of "
      "arrival, the apathy, the hunger—and the prisoners who gave away their last piece of bread. Those most likely "
      "to endure, he observed, were those who had something to live for. The second part introduces logotherapy: "
      "meaning can be found in creating a work or doing a deed, in loving someone, and in the attitude we take "
      "toward unavoidable suffering. It has sold many millions of copies worldwide.",
      ["The last human freedom is to choose one's attitude in any circumstances.",
       "Meaning comes from work, from love and from courage in suffering.",
       "Those who have a 'why' to live can bear almost any 'how'."],
      original="…trotzdem Ja zum Leben sagen", featured=True),
    W("the-second-sex", "The Second Sex", "simone-de-beauvoir", 1949, "book", "French", 800, 3,
      ["political-philosophy", "ethics", "society-and-economics"],
      "'One is not born, but rather becomes, a woman.' Beauvoir's monumental study of women's oppression.",
      "Beauvoir asks 'What is a woman?' and answers that, throughout history, woman has been defined as man's "
      "Other—the inessential, the object. Volume one examines biology, psychoanalysis, Marxism, history and myth; "
      "volume two follows women's lived experience from childhood through marriage, motherhood and old age, showing "
      "how femininity is constructed. Placed on the Vatican's Index of Forbidden Books, it became a founding text "
      "of modern feminism.",
      ["One is not born, but rather becomes, a woman.",
       "Woman has been constructed as the Other to man's Subject.",
       "Liberation requires economic independence and freedom to pursue one's own projects."],
      original="Le Deuxième Sexe", featured=True),
    W("the-ethics-of-ambiguity", "The Ethics of Ambiguity", "simone-de-beauvoir", 1947, "essay", "French", 160, 3,
      ["ethics", "meaning-of-life"],
      "Beauvoir's answer to the charge that existentialism can't ground ethics: my freedom requires the freedom of "
      "others.",
      "Beauvoir begins with the 'tragic ambiguity' of the human condition: we are both free subjects and objects "
      "among things, mortal yet aware of it. Rather than deny this ambiguity, we must assume it. She portrays types "
      "who flee freedom—the sub-man, the serious man, the nihilist, the adventurer—and argues that to will oneself "
      "free is also to will others free. It is arguably the most complete existentialist ethics.",
      ["The human condition is fundamentally ambiguous.",
       "To will oneself free is also to will others free.",
       "The 'serious man' hides from freedom behind absolute values."],
      original="Pour une morale de l'ambiguïté"),
    W("gravity-and-grace", "Gravity and Grace", "simone-weil", 1947, "aphorisms", "French", 200, 3,
      ["philosophy-of-religion", "ethics"],
      "Aphorisms from Simone Weil's notebooks on attention, affliction, detachment and the void.",
      "Compiled after Weil's death by her friend Gustave Thibon from her notebooks, Gravity and Grace collects "
      "brief, intense reflections. 'Gravity' is the downward pull of self-interest and force that governs the soul "
      "as it governs matter; 'grace' alone can lift it. Weil writes of attention as prayer, of 'decreation'—the "
      "undoing of the ego—and of affliction as both a horror and an opening to God. Uncompromising and luminous, "
      "it is one of the great spiritual books of the century.",
      ["Pure, undivided attention is the essence of prayer and of love.",
       "The soul is subject to a moral gravity; only grace lifts it.",
       "'Decreation': we must give up the ego to receive what is real."],
      original="La Pesanteur et la grâce"),
    W("two-concepts-of-liberty", "Two Concepts of Liberty", "isaiah-berlin", 1958, "lectures", "English", 60, 2,
      ["political-philosophy"],
      "Berlin's lecture distinguishing 'negative' from 'positive' liberty—and warning of the latter's abuses.",
      "Delivered as his inaugural lecture at Oxford in 1958, this essay distinguishes negative liberty—freedom from "
      "interference—from positive liberty—self-mastery, being one's own master. Berlin shows how the positive "
      "idea, though noble, has been twisted to justify coercing people for the sake of their 'true' selves. He "
      "ends with a defence of value pluralism: human goods are many and may conflict, so no final solution can "
      "reconcile them all.",
      ["Negative liberty is freedom from interference by others.",
       "Positive liberty, as self-mastery, can be twisted into coercion.",
       "Values are plural and can genuinely conflict."]),
    W("the-hedgehog-and-the-fox", "The Hedgehog and the Fox", "isaiah-berlin", 1953, "essay", "English", 100, 2,
      ["history"],
      "Berlin's famous essay on Tolstoy: the fox knows many things, but the hedgehog knows one big thing.",
      "Taking a fragment of the Greek poet Archilochus as his starting point, Berlin divides thinkers into "
      "hedgehogs, who relate everything to a single central vision (Plato, Dante, Hegel), and foxes, who pursue "
      "many ends, often unrelated (Aristotle, Shakespeare, Montaigne). Tolstoy, he argues, was by nature a fox who "
      "believed in being a hedgehog. The essay is really about Tolstoy's philosophy of history in War and Peace, but "
      "its typology took on a life of its own.",
      ["Hedgehogs see the world through one big idea; foxes through many.",
       "Tolstoy was a fox by nature who longed to be a hedgehog.",
       "Grand theories of history struggle against the variety of human experience."]),
    W("the-myth-of-sisyphus", "The Myth of Sisyphus", "albert-camus", 1942, "essay", "French", 130, 2,
      ["meaning-of-life", "ethics"],
      "Is life worth living in a meaningless universe? Camus answers with revolt, freedom and passion.",
      "Camus opens with what he calls the one truly serious philosophical problem: whether life is worth living. "
      "The absurd arises from the confrontation between our demand for meaning and the 'unreasonable silence of "
      "the world'. Rejecting both suicide and the 'leap' into religious hope, he argues for living with the absurd "
      "in lucid revolt. The closing image of Sisyphus, condemned forever to roll a rock uphill, becomes an image of "
      "human dignity: 'one must imagine Sisyphus happy'.",
      ["The absurd is the clash between our longing for meaning and the world's silence.",
       "Refuse both suicide and false hope; live in lucid revolt.",
       "One must imagine Sisyphus happy."],
      original="Le Mythe de Sisyphe", featured=True),
    W("the-stranger", "The Stranger", "albert-camus", 1942, "novel", "French", 120, 1,
      ["meaning-of-life", "ethics"],
      "Meursault, an indifferent clerk in Algiers, kills a man on a beach—and is condemned as much for not weeping "
      "at his mother's funeral.",
      "'Mother died today. Or maybe yesterday; I can't be sure.' Camus' first novel follows Meursault, who refuses "
      "to pretend to feelings he does not have. After he shoots a man on a sun-blasted beach, his trial becomes a "
      "judgement of his character. Awaiting execution, he opens himself to 'the gentle indifference of the world'. "
      "A literary companion to The Myth of Sisyphus, it is among the most widely read French novels of the century.",
      ["Society demands conventional feelings and punishes those who refuse to perform them.",
       "Honesty about one's experience can be a kind of integrity.",
       "Accepting the world's indifference can bring a strange peace."],
      original="L'Étranger"),
    W("the-rebel", "The Rebel", "albert-camus", 1951, "essay", "French", 300, 3,
      ["political-philosophy", "ethics"],
      "Camus traces how revolt against injustice can turn into murderous revolution—and how to keep it humane.",
      "Where The Myth of Sisyphus asked about suicide, The Rebel asks about murder. Rebellion begins as a 'no' that "
      "affirms a shared human dignity—'I rebel, therefore we exist'. But history shows revolt hardening into "
      "systems that justify killing in the name of the future. Camus argues for limits and moderation. The book "
      "precipitated his famous break with Sartre.",
      ["I rebel—therefore we exist: revolt affirms a shared human dignity.",
       "Revolutions that justify murder betray rebellion's origin.",
       "True rebellion respects limits."],
      original="L'Homme révolté"),
    W("the-sovereignty-of-good", "The Sovereignty of Good", "iris-murdoch", 1970, "essay", "English", 110, 3,
      ["ethics"],
      "Three essays arguing that morality is about loving attention to reality, not just choices.",
      "Murdoch challenges both the existentialist hero and the analytic moral philosopher, who picture the moral "
      "agent as a will choosing in a void. Most of morality happens between choices, in how we see: her example of "
      "a mother-in-law who gradually learns to see her daughter-in-law justly has become famous. Drawing on Plato "
      "and Simone Weil, she argues that the Good is real and that art and attention can lift us out of the 'fat "
      "relentless ego'.",
      ["Morality is largely a matter of attention: seeing others justly and lovingly.",
       "The 'fat relentless ego' is the chief enemy of moral life.",
       "The Good is real and transcendent, like the sun in Plato's cave."]),
    W("the-structure-of-scientific-revolutions", "The Structure of Scientific Revolutions", "thomas-kuhn", 1962,
      "book", "English", 210, 3, ["philosophy-of-science", "history"],
      "Kuhn's argument that science advances not steadily but through revolutionary 'paradigm shifts'.",
      "Kuhn describes 'normal science' as puzzle-solving within a paradigm—an accepted framework such as Newtonian "
      "mechanics. Anomalies accumulate until a crisis provokes a revolution and a new paradigm, as with "
      "Copernicus, Lavoisier or Einstein. Competing paradigms are partly 'incommensurable', so the change resembles "
      "a gestalt switch more than a step-by-step proof. Controversial among philosophers, the book transformed how "
      "we think about science and gave everyday speech the 'paradigm shift'.",
      ["Normal science solves puzzles within a paradigm.",
       "Anomalies lead to crisis and revolutionary paradigm shifts.",
       "Rival paradigms are partly incommensurable."],
      featured=True),
    W("a-theory-of-justice", "A Theory of Justice", "john-rawls", 1971, "treatise", "English", 560, 4,
      ["political-philosophy", "ethics"],
      "Choose principles of justice behind a 'veil of ignorance': Rawls' case for justice as fairness.",
      "Rawls revives social contract theory to find principles for the basic structure of society. Imagine "
      "choosing them in an 'original position', behind a veil of ignorance that hides your class, talents, race, "
      "gender and conception of the good. Rawls argues you would choose equal basic liberties for all, and permit "
      "inequalities only if they attach to positions open to all under fair equality of opportunity and benefit "
      "the least advantaged (the difference principle). It is the central text of modern political philosophy.",
      ["Justice is the first virtue of social institutions.",
       "The veil of ignorance models fairness in choosing principles.",
       "The difference principle: inequalities must benefit the least advantaged."],
      featured=True),
    W("the-wretched-of-the-earth", "The Wretched of the Earth", "frantz-fanon", 1961, "book", "French", 300, 3,
      ["political-philosophy", "society-and-economics", "philosophy-of-mind"],
      "Fanon's searing analysis of colonialism, violence, national consciousness and the psychological wounds of "
      "empire.",
      "Written in the final months of Fanon's life during the Algerian War, The Wretched of the Earth analyses "
      "colonialism as a system of violence that can only be undone through struggle. Fanon warns of the 'pitfalls "
      "of national consciousness'—that a new national elite might simply replace the colonial rulers—and closes "
      "with psychiatric case studies of the war's trauma. With a preface by Sartre, it became a handbook for "
      "anticolonial movements worldwide.",
      ["Colonialism is a system of violence that shapes body and mind.",
       "Independence may be betrayed by a new national elite.",
       "Each generation must discover its mission, fulfil it, or betray it."],
      original="Les Damnés de la Terre"),
    W("discipline-and-punish", "Discipline and Punish", "michel-foucault", 1975, "book", "French", 330, 4,
      ["political-philosophy", "history", "society-and-economics"],
      "From the scaffold to the prison: Foucault's history of how modern power disciplines bodies and minds.",
      "Foucault opens with the gruesome public execution of the would-be regicide Damiens in 1757, then shows how, "
      "within a century, punishment moved from spectacle to the prison timetable. The new 'disciplinary power' "
      "works through surveillance, examination and normalisation—in prisons, but also in schools, factories, "
      "barracks and hospitals. Bentham's Panopticon, in which inmates never know whether they are being watched, "
      "becomes the diagram of modern society.",
      ["Modern power disciplines bodies through surveillance and normalisation.",
       "The Panopticon: being always visible makes people police themselves.",
       "Power and knowledge are intertwined."],
      original="Surveiller et punir", featured=True),
    W("anarchy-state-and-utopia", "Anarchy, State, and Utopia", "robert-nozick", 1974, "book", "English", 350, 4,
      ["political-philosophy"],
      "Nozick's libertarian answer to Rawls: only a minimal state can be justified.",
      "Nozick begins from the premise that individuals have rights so strong that they raise the question of what, "
      "if anything, the state may do. He argues that a minimal 'night-watchman' state could arise from anarchy "
      "without violating anyone's rights, but that any more extensive state—including one that redistributes "
      "wealth—does violate them. His Wilt Chamberlain example challenges patterned theories of justice, and the "
      "book also introduced the 'experience machine' thought experiment.",
      ["Individuals have rights that limit what the state may do.",
       "Only a minimal state is justified; redistribution violates rights.",
       "Justice in holdings depends on history, not on patterns."]),
    W("what-is-it-like-to-be-a-bat", "What Is It Like to Be a Bat?", "thomas-nagel", 1974, "essay", "English", 20,
      3, ["philosophy-of-mind"],
      "Nagel's landmark essay: no physical description can capture the subjective character of experience.",
      "Bats navigate by echolocation, a sense utterly unlike ours. Even if we knew everything about bat "
      "neurophysiology, Nagel argues, we would not know what it is like for the bat. Conscious experience has an "
      "essentially subjective character, tied to a point of view, which the objective methods of physical science "
      "leave out. Published in The Philosophical Review, it remains a cornerstone of the debate about "
      "consciousness and the mind–body problem.",
      ["An organism is conscious if there is something it is like to be that organism.",
       "Subjective experience is tied to a single point of view.",
       "Physicalism cannot yet explain the subjective character of experience."]),
    W("animal-liberation", "Animal Liberation", "peter-singer", 1975, "book", "English", 320, 2,
      ["ethics"],
      "Singer's book that launched the modern animal rights movement, arguing against 'speciesism'.",
      "Singer argues that the capacity to suffer, not species membership, is what gives a being moral standing. "
      "Discriminating against animals simply because they are not human—'speciesism'—is a prejudice like racism "
      "or sexism. He documents factory farming and animal experimentation in detail and makes the case for "
      "vegetarianism. Revised as Animal Liberation Now in 2023, it remains one of the most influential works of "
      "applied ethics.",
      ["The capacity to suffer is the key to moral consideration.",
       "Speciesism is a prejudice like racism or sexism.",
       "Factory farming causes immense, unjustifiable suffering."]),
    W("sophies-world", "Sophie's World", "jostein-gaarder", 1991, "novel", "Norwegian", 520, 1,
      ["meaning-of-life", "history"],
      "A girl receives mysterious letters asking 'Who are you?'—and is drawn into the whole history of philosophy.",
      "Fourteen-year-old Sophie Amundsen finds a note in her mailbox: 'Who are you?' Then another: 'Where does the "
      "world come from?' Soon a mysterious philosopher, Alberto Knox, is sending her a correspondence course from "
      "the Presocratics to Sartre. But strange things keep happening, and Sophie begins to suspect that her own "
      "world is not what it seems. Both a mystery novel and a gentle introduction to Western philosophy, it became "
      "one of the bestselling books of the 1990s.",
      ["Philosophy begins in wonder—a capacity children have and adults often lose.",
       "The history of philosophy is a living conversation.",
       "Questioning your own reality is the first step toward wisdom."],
      original="Sofies verden", featured=True),
    W("guns-germs-and-steel", "Guns, Germs, and Steel", "jared-diamond", 1997, "book", "English", 480, 2,
      ["history", "society-and-economics"],
      "Why did Eurasian societies conquer others? Diamond's answer lies in geography, not genes.",
      "Diamond argues that the different fates of human societies over the past 13,000 years stem from "
      "environmental differences, not innate differences between peoples. Eurasia had more domesticable plants and "
      "animals and an east–west axis along which crops spread easily; farming produced dense populations, "
      "specialists, writing, states and immunity to epidemic diseases. Those advantages help explain, for example, "
      "the Spanish conquest of the Inca. It won the Pulitzer Prize and remains widely debated by historians.",
      ["Geography and environment, not race, shaped the fates of societies.",
       "Food production enabled dense populations, states and technology.",
       "Epidemic diseases from domesticated animals shaped the course of conquest."],
      featured=True),
    W("sapiens", "Sapiens: A Brief History of Humankind", "yuval-noah-harari", 2011, "book", "Hebrew", 450, 1,
      ["history", "society-and-economics", "meaning-of-life"],
      "From insignificant ape to ruler of the planet: Harari's sweeping history of our species.",
      "Harari organises human history around three revolutions: the Cognitive Revolution, around 70,000 years "
      "ago, when Sapiens became able to cooperate flexibly in large numbers through shared fictions; the "
      "Agricultural Revolution, which he provocatively calls history's biggest fraud; and the Scientific "
      "Revolution, which gave us unprecedented power. Accessible and argumentative, it asks whether all this power "
      "has made us any happier.",
      ["Shared fictions—myths, money, nations—let humans cooperate at scale.",
       "The Agricultural Revolution made life harder for most individuals.",
       "Greater power has not obviously made humans happier."],
      original="קיצור תולדות האנושות", featured=True),
]
