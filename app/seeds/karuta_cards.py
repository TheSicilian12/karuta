from app.models import db, karuta_cards, environment, SCHEMA;
from sqlalchemy.sql import text;

def seed_karuta_cards():
    # card1 = karuta_cards(
    #     english_line1 = "",
    #     english_line2 = "",
    #     english_line3 = "",
    #     english_line4 = "",
    #     english_line5 = "",
    #     english_author = "",

    #     japanese_line1 = "",
    #     japanese_line2 = "",
    #     japanese_line3 = "",
    #     japanese_line4 = "",
    #     japanese_line5 = "",
    #     japanese_author = "",

    #     romaji_line1 = "",
    #     romaji_line2 = "",
    #     romaji_line3 = "",
    #     romaji_line4 = "",
    #     romaji_line5 = "",
    #     romaji_author = "",
    # )

    card1 = karuta_cards(
        english_line1 = 'Coarse the rush-mat roof',
        english_line2 = 'Sheltering the harvest-hut',
        english_line3 = 'Of the autumn rice-field;',
        english_line4 = 'And my sleeves are growing wet',
        english_line5 = 'With the moisture dripping through.',
        english_author = 'Emperor Tenchi',

        japanese_line1 = '秋の田の',
        japanese_line2 = 'かりほの庵の',
        japanese_line3 = '苫をあらみ',
        japanese_line4 = 'わが衣手は',
        japanese_line5 = '露にぬれつつ',
        japanese_author = '天智天皇',

        romaji_line1 = 'Aki no ta no',
        romaji_line2 = 'Kariho no io no',
        romaji_line3 = 'Toma o arami',
        romaji_line4 = 'Waga koromode wa',
        romaji_line5 = 'Tsuyu ni nure tsutsu',
        romaji_author = 'Tenchi Tenno',
    )
    card2 = karuta_cards(
        english_line1 = 'The spring has passed',
        english_line2 = 'And the summer come again;',
        english_line3 = 'For the silk-white robes,',
        english_line4 = 'So they say, are spread to dry',
        english_line5 = 'On the "Mount of Heaven\'s Perfume."',
        english_author = 'Empress Jito',

        japanese_line1 = '春過ぎて',
        japanese_line2 = '夏来にけらし',
        japanese_line3 = '白妙の',
        japanese_line4 = '衣ほすてふ',
        japanese_line5 = '天の香具山',
        japanese_author = '持統天皇',

        romaji_line1 = 'Haru sugite',
        romaji_line2 = 'Natsu ki ni kerashi',
        romaji_line3 = 'Shirotae no',
        romaji_line4 = 'Koromo hosu cho',
        romaji_line5 = 'Ama no Kaguyama',
        romaji_author = 'Jito Tenno',
    )
    card3 = karuta_cards(
        english_line1='Oh, the foot-drawn trail',
        english_line2="Of the mountain-pheasant's tail",
        english_line3='Drooped like down-curved branch!',
        english_line4='Through this long, long-dragging night',
        english_line5='Must I lie in bed alone?',
        english_author='Kakinomoto no Hitomaro',

        japanese_line1='あしびきの',
        japanese_line2='山鳥の尾の',
        japanese_line3='しだり尾の',
        japanese_line4='ながながし夜を',
        japanese_line5='ひとりかもねむ',
        japanese_author='柿本人麿',

        romaji_line1='Ashibiki no',
        romaji_line2='Yamadori no o no',
        romaji_line3='Shidari o no',
        romaji_line4='Naganagashi yo o',
        romaji_line5='Hitori ka mo nen',
        romaji_author='Kakinomoto no Hitomaro',
    )
    card4 = karuta_cards(
        english_line1 = 'When I take the path',
        english_line2 = "To Tago's coast, I see",
        english_line3 = 'Perfect whiteness laid',
        english_line4 = "On Mount Fuji's lofty peak",
        english_line5 = 'By the drift of falling snow.',
        english_author = 'Yamabe no Akahito',

        japanese_line1 = '田子の浦に',
        japanese_line2 = '打ち出でてみれば',
        japanese_line3 = '白妙の',
        japanese_line4 = '富士の高嶺に',
        japanese_line5 = '雪はふりつつ',
        japanese_author = '山辺赤人',

        romaji_line1 = 'Tago no Ura ni',
        romaji_line2 = 'Uchi idete mireba',
        romaji_line3 = 'Shirotae no',
        romaji_line4 = 'Fuji no takane ni',
        romaji_line5 = 'Yuki wa furi tsutsu',
        romaji_author = 'Yamabe no Akahito',
    )
    card5 = karuta_cards(
        english_line1 = 'In the mountain depths,',
        english_line2 = 'Treading through the crimson leaves,',
        english_line3 = 'The wandering stag calls.',
        english_line4 = 'When I hear the lonely cry,',
        english_line5 = 'Sad--how sad!--the autumn is.',
        english_author = 'Sarumaru',

        japanese_line1 = '奥山に',
        japanese_line2 = '紅葉ふみわけ',
        japanese_line3 = '鳴く鹿の',
        japanese_line4 = '声きく時ぞ',
        japanese_line5 = '秋は悲しき',
        japanese_author = '猿丸大夫',

        romaji_line1 = 'Okuyama ni',
        romaji_line2 = 'Momiji fumiwake',
        romaji_line3 = 'Naku shika no',
        romaji_line4 = 'Koe kiku toki zo',
        romaji_line5 = 'Aki wa kanashiki',
        romaji_author = 'Sarumaru Dayu',
    )
    card6 = karuta_cards(
        english_line1 = 'If I see that bridge',
        english_line2 = 'That is spanned by flights of magpies',
        english_line3 = 'Across the arc of heaven',
        english_line4 = 'Made white with a deep-laid frost,',
        english_line5 = 'Then the night is almost past.',
        english_author = 'Otomo no Yakamochi',

        japanese_line1 = 'かささぎの',
        japanese_line2 = '渡せる橋に',
        japanese_line3 = '置く霜の',
        japanese_line4 = '白きを見れば',
        japanese_line5 = '夜ぞふけにける',
        japanese_author = '中納言家持',

        romaji_line1 = 'Kasasagi no',
        romaji_line2 = 'Wataseru hashi ni',
        romaji_line3 = 'Oku shimo no',
        romaji_line4 = 'Shiroki o mireba',
        romaji_line5 = 'Yo zo fuke ni keru',
        romaji_author = 'Chunagon Yakamochi',
    )
    card7 = karuta_cards(
        english_line1 = 'When I look up at',
        english_line2 = 'The wide-stretched plain of heaven,',
        english_line3 = 'Is the moon the same',
        english_line4 = 'That rose on Mount Mikasa',
        english_line5 = 'In the land of Kasuga?',
        english_author = 'Abe no Nakamaro',

        japanese_line1 = '天の原',
        japanese_line2 = 'ふりさけ見れば',
        japanese_line3 = '春日なる',
        japanese_line4 = '三笠の山に',
        japanese_line5 = '出でし月かも',
        japanese_author = '安倍仲麿',

        romaji_line1 = 'Ama no hara',
        romaji_line2 = 'Furisake mireba',
        romaji_line3 = 'Kasuga naru',
        romaji_line4 = 'Mikasa no yama ni',
        romaji_line5 = 'Ideshi tsuki kamo',
        romaji_author = 'Abe no Nakamaro',
    )
    card8 = karuta_cards(
        english_line1 = 'My lowly hut is',
        english_line2 = 'Southeast from the capital.',
        english_line3 = 'Thus I choose to live.',
        english_line4 = 'And the world in which I live',
        english_line5 = 'Men have named a "Mount of Gloom."',
        english_author = 'The Monk Kisen',

        japanese_line1 = 'わが庵は',
        japanese_line2 = '都のたつみ',
        japanese_line3 = 'しかぞすむ',
        japanese_line4 = '世をうぢ山と',
        japanese_line5 = '人はいふなり',
        japanese_author = '喜撰法師',

        romaji_line1 = 'Waga io wa',
        romaji_line2 = 'Miyako no tatsumi',
        romaji_line3 = 'Shika zo sumu',
        romaji_line4 = 'Yo o Ujiyama to',
        romaji_line5 = 'Hito wa iu nari',
        romaji_author = 'Kisen Hoshi',
    )
    card9 = karuta_cards(
        english_line1 = 'Color of the flower',
        english_line2 = 'Has already faded away,',
        english_line3 = 'While in idle thoughts',
        english_line4 = 'My life passes vainly by,',
        english_line5 = 'As I watch the long rains fall.',
        english_author = 'Ono no Komachi',

        japanese_line1 = '花の色は',
        japanese_line2 = 'うつりにけりな',
        japanese_line3 = 'いたづらに',
        japanese_line4 = 'わが身世にふる',
        japanese_line5 = 'ながめせしまに',
        japanese_author = '小野小町',

        romaji_line1 = 'Hana no iro wa',
        romaji_line2 = 'Utsuri ni keri na',
        romaji_line3 = 'Itazura ni',
        romaji_line4 = 'Waga mi yo ni furu',
        romaji_line5 = 'Nagame seshi ma ni',
        romaji_author = 'Ono no Komachi',
    )
    card10 = karuta_cards(
        english_line1 = 'Truly, this is where',
        english_line2 = 'Travelers who go or come',
        english_line3 = 'Over parting ways--',
        english_line4 = 'Friends or strangers--all must meet:',
        english_line5 = 'The gate of "Meeting Hill."',
        english_author = 'Semimaru',

        japanese_line1 = 'これやこの',
        japanese_line2 = '行くも帰るも',
        japanese_line3 = '別れては',
        japanese_line4 = '知るも知らぬも',
        japanese_line5 = '逢坂の関',
        japanese_author = '蝉丸',

        romaji_line1 = 'Kore ya kono',
        romaji_line2 = 'Yuku mo kaeru mo',
        romaji_line3 = 'Wakarete wa',
        romaji_line4 = 'Shiru mo shiranu mo',
        romaji_line5 = 'Osaka no seki',
        romaji_author = 'Semimaru',
    )
    card11 = karuta_cards(
        english_line1 = 'Over the wide sea',
        english_line2 = 'Towards its many distant isles',
        english_line3 = 'My ship sets sail.',
        english_line4 = 'Will the fishing boats thronged here',
        english_line5 = 'Proclaim my journey to the world?',
        english_author = 'Ono no Takamura',

        japanese_line1 = 'わたの原',
        japanese_line2 = '八十島かけて',
        japanese_line3 = 'こぎ出ぬと',
        japanese_line4 = '人には告げよ',
        japanese_line5 = 'あまのつり舟',
        japanese_author = '参議篁',

        romaji_line1 = 'Wata no hara',
        romaji_line2 = 'Yasoshima kakete',
        romaji_line3 = 'Kogi idenu to',
        romaji_line4 = 'Hito ni wa tsugeyo',
        romaji_line5 = 'Ama no tsuri bune',
        romaji_author = 'Sangi Takamura',
    )
    card12 = karuta_cards(
        english_line1 = 'Let the winds of heaven',
        english_line2 = 'Blow through the paths among the clouds',
        english_line3 = 'And close their gates.',
        english_line4 = 'Then for a while I could detain',
        english_line5 = 'These messengers in maiden form.',
        english_author = 'The Monk Henjo',

        japanese_line1 = '天つ風',
        japanese_line2 = '雲のかよひ路',
        japanese_line3 = '吹きとぢよ',
        japanese_line4 = '乙女のすがた',
        japanese_line5 = 'しばしとどめむ',
        japanese_author = '僧正遍昭',

        romaji_line1 = 'Ama tsu kaze',
        romaji_line2 = 'Kumo no kayoiji',
        romaji_line3 = 'Fuki toji yo',
        romaji_line4 = 'Otome no sugata',
        romaji_line5 = 'Shibashi todomen',
        romaji_author = 'Sojo Henjo',
    )
    card13 = karuta_cards(
        english_line1 = "From Tsukuba's peak",
        english_line2 = 'Falling waters have become',
        english_line3 = "Mina's still, full flow:",
        english_line4 = 'So my love has grown to be',
        english_line5 = "Like the river's quiet deeps.",
        english_author = 'Emperor Yozei',

        japanese_line1 = '筑波嶺の',
        japanese_line2 = '峰より落つる',
        japanese_line3 = 'みなの川',
        japanese_line4 = '恋ぞつもりて',
        japanese_line5 = '淵となりぬる',
        japanese_author = '陽成院',

        romaji_line1 = 'Tsukuba ne no',
        romaji_line2 = 'Mine yori otsuru',
        romaji_line3 = 'Minano-gawa',
        romaji_line4 = 'Koi zo tsumorite',
        romaji_line5 = 'Fuchi to nari nuru',
        romaji_author = 'Yozei In',
    )
    card14 = karuta_cards(
        english_line1 = 'Like Michinoku prints',
        english_line2 = 'Of the tangled leaves of ferns,',
        english_line3 = 'It is because of you',
        english_line4 = 'That I have become confused;',
        english_line5 = 'But my love for you remains.',
        english_author = 'Minamoto no Toru',

        japanese_line1 = 'みちのくの',
        japanese_line2 = 'しのぶもぢずり',
        japanese_line3 = '誰故に',
        japanese_line4 = '乱れそめにし',
        japanese_line5 = '我ならなくに',
        japanese_author = '河原左大臣',

        romaji_line1 = 'Michinoku no',
        romaji_line2 = 'Shinobu moji-zuri',
        romaji_line3 = 'Tare yue ni',
        romaji_line4 = 'Midare some ni shi',
        romaji_line5 = 'Ware naranaku ni',
        romaji_author = 'Kawara no Sadaijin',
    )
    card15 = karuta_cards(
        english_line1 = 'It is for your sake',
        english_line2 = 'That I walk the fields in spring,',
        english_line3 = 'Gathering green herbs,',
        english_line4 = "While my garment's hanging sleeves",
        english_line5 = 'Are speckled with falling snow.',
        english_author = 'Emperor Koko',

        japanese_line1 = '君がため',
        japanese_line2 = '春の野に出でて',
        japanese_line3 = '若菜つむ',
        japanese_line4 = 'わが衣手に',
        japanese_line5 = '雪はふりつつ',
        japanese_author = '光孝天皇',

        romaji_line1 = 'Kimi ga tame',
        romaji_line2 = 'Haru no no ni idete',
        romaji_line3 = 'Wakana tsumu',
        romaji_line4 = 'Waga koromode ni',
        romaji_line5 = 'Yuki wa furi tsutsu',
        romaji_author = 'Koko Tenno',
    )
    card16 = karuta_cards(
        english_line1 = 'Though we are parted,',
        english_line2 = "If on Mount Inaba's peak",
        english_line3 = 'I should hear the sound',
        english_line4 = 'Of the pine trees growing there,',
        english_line5 = "I'll come back again to you.",
        english_author = 'Ariwara no Yukihira',

        japanese_line1 = '立ち別れ',
        japanese_line2 = 'いなばの山の',
        japanese_line3 = '峰に生ふる',
        japanese_line4 = 'まつとしきかば',
        japanese_line5 = '今かへりこむ',
        japanese_author = '中納言行平',

        romaji_line1 = 'Tachi wakare',
        romaji_line2 = 'Inaba no yama no',
        romaji_line3 = 'Mine ni oru',
        romaji_line4 = 'Matsu to shi kikaba',
        romaji_line5 = 'Ima kaeri kon',
        romaji_author = 'Chunagon Yukihira',
    )
    card17 = karuta_cards(
        english_line1 = 'Even when the gods',
        english_line2 = 'Held sway in the ancient days,',
        english_line3 = 'I have never heard',
        english_line4 = 'That water gleamed with autumn red',
        english_line5 = "As it does in Tatta's stream",
        english_author = 'Ariwara no Narihira',

        japanese_line1 = '千早ぶる',
        japanese_line2 = '神代もきかず',
        japanese_line3 = '龍田川',
        japanese_line4 = 'からくれないに',
        japanese_line5 = '水くくるとは',
        japanese_author = '在原業平朝臣',

        romaji_line1 = 'Chihayaburu',
        romaji_line2 = 'Kamiyo mo kikazu',
        romaji_line3 = 'Tatsuta-gawa',
        romaji_line4 = 'Kara kurenai ni',
        romaji_line5 = 'Mizu kukuru to wa',
        romaji_author = 'Ariwara no Narihira Ason',
    )
    card18 = karuta_cards(
        english_line1 = 'The waves are gathered',
        english_line2 = 'On the shore of Sumi Bay,',
        english_line3 = 'And in the gathered night,',
        english_line4 = 'When in dreams I go to you,',
        english_line5 = "I hide from people's eyes.",
        english_author = 'Fujiwara no Toshiyuki',

        japanese_line1 = '住の江の',
        japanese_line2 = '岸による波',
        japanese_line3 = 'よるさへや',
        japanese_line4 = '夢の通ひ路',
        japanese_line5 = '人目よくらむ',
        japanese_author = '藤原敏行朝臣',

        romaji_line1 = 'Sumi no e no',
        romaji_line2 = 'Kishi ni yoru nami',
        romaji_line3 = 'Yoru sae ya',
        romaji_line4 = 'Yume no kayoi ji',
        romaji_line5 = 'Hito me yoku ran',
        romaji_author = 'Fujiwara no Toshiyuki Ason',
    )
    card19 = karuta_cards(
        english_line1 = 'Even for a time',
        english_line2 = 'Short as a piece of the reeds',
        english_line3 = "In Naniwa's marsh,",
        english_line4 = 'We must never meet again:',
        english_line5 = 'Is this what you are asking me?',
        english_author = 'Lady Ise',

        japanese_line1 = '難波潟',
        japanese_line2 = 'みじかき芦の',
        japanese_line3 = 'ふしのまも',
        japanese_line4 = 'あはでこの世を',
        japanese_line5 = '過ぐしてよとや',
        japanese_author = '伊勢',

        romaji_line1 = 'Naniwa gata',
        romaji_line2 = 'Mijikaki ashi no',
        romaji_line3 = 'Fushi no ma mo',
        romaji_line4 = 'Awade kono yo o',
        romaji_line5 = 'Sugushite yo to ya',
        romaji_author = 'Ise',
    )
    card20 = karuta_cards(
        english_line1 = 'In this dire distress',
        english_line2 = 'My life is meaningless.',
        english_line3 = 'So we must meet now,',
        english_line4 = 'Even though it costs my life',
        english_line5 = 'In the Bay of Naniwa.',
        english_author = 'Prince Motoyoshi',

        japanese_line1 = 'わびぬれば',
        japanese_line2 = '今はた同じ',
        japanese_line3 = '難波なる',
        japanese_line4 = '身をつくしても',
        japanese_line5 = '逢はむとぞ思ふ',
        japanese_author = '元良親王',

        romaji_line1 = 'Wabi nureba',
        romaji_line2 = 'Ima hata onaji',
        romaji_line3 = 'Naniwa naru',
        romaji_line4 = 'Mi o tsukushite mo',
        romaji_line5 = 'Awan to zo omou',
        romaji_author = 'Motoyoshi Shinno',
    )
    card21 = karuta_cards(
        english_line1 = 'Just because she said,',
        english_line2 = '"In a moment I will come,"',
        english_line3 = "I've awaited her",
        english_line4 = 'Until the moon of daybreak,',
        english_line5 = 'In the long month, has appeared.',
        english_author = 'The Monk Sosei',

        japanese_line1 = '今来むと',
        japanese_line2 = 'いひしばかりに',
        japanese_line3 = '長月の',
        japanese_line4 = '有明の月を',
        japanese_line5 = '待ち出でつるかな',
        japanese_author = '素性法師',

        romaji_line1 = 'Ima kon to',
        romaji_line2 = 'Iishi bakari ni',
        romaji_line3 = 'Nagatsuki no',
        romaji_line4 = 'Ariake no tsuki o',
        romaji_line5 = 'Machi idetsuru kana',
        romaji_author = 'Sosei Hoshi',
    )
    card22 = karuta_cards(
        english_line1 = 'It is by its breath',
        english_line2 = "That autumn's leaves of trees and grass",
        english_line3 = 'Are wasted and driven.',
        english_line4 = 'So they call this mountain wind',
        english_line5 = 'The wild one, the destroyer.',
        english_author = "Fun'ya no Yasuhide",

        japanese_line1 = '吹くからに',
        japanese_line2 = '秋の草木の',
        japanese_line3 = 'しをるれば',
        japanese_line4 = 'むべ山風を',
        japanese_line5 = 'あらしといふらむ',
        japanese_author = '文屋康秀',

        romaji_line1 = 'Fuku kara ni',
        romaji_line2 = 'Aki no kusaki no',
        romaji_line3 = 'Shiorureba',
        romaji_line4 = 'Mube yama kaze o',
        romaji_line5 = 'Arashi to iuran',
        romaji_author = "Fun'ya no Yasuhide",
    )
    card23 = karuta_cards(
        english_line1 = 'As I view the moon,',
        english_line2 = 'Many things come into my mind,',
        english_line3 = 'And my thoughts are sad;',
        english_line4 = "Yet it's not for me alone,",
        english_line5 = 'That the autumn time has come.',
        english_author = 'Oe no Chisato',

        japanese_line1 = '月見れば',
        japanese_line2 = '千々に物こそ',
        japanese_line3 = '悲しけれ',
        japanese_line4 = 'わが身ひとつの',
        japanese_line5 = '秋にはあらねど',
        japanese_author = '大江千里',

        romaji_line1 = 'Tsuki mireba',
        romaji_line2 = 'Chiji ni mono koso',
        romaji_line3 = 'Kanashi kere',
        romaji_line4 = 'Waga mi hitotsu no',
        romaji_line5 = 'Aki ni wa aranedo',
        romaji_author = 'Oe no Chisato',
    )
    card24 = karuta_cards(
        english_line1 = 'At the present time,',
        english_line2 = 'Since I could bring no offering,',
        english_line3 = 'See Mount Tamuke!',
        english_line4 = 'Here are brocades of red leaves,',
        english_line5 = 'As a tribute to the gods.',
        english_author = 'Sugawara no Michizane',

        japanese_line1 = 'このたびは',
        japanese_line2 = '幣もとりあへず',
        japanese_line3 = '手向山',
        japanese_line4 = '紅葉のにしき',
        japanese_line5 = '神のまにまに',
        japanese_author = '菅家',

        romaji_line1 = 'Kono tabi wa',
        romaji_line2 = 'Nusa mo toriaezu',
        romaji_line3 = 'Tamukeyama',
        romaji_line4 = 'Momiji no nishiki',
        romaji_line5 = 'Kami no mani mani',
        romaji_author = 'Kan Ke',
    )
    card25 = karuta_cards(
        english_line1 = 'If your name is true,',
        english_line2 = 'Trailing vine of "Meeting Hill,"',
        english_line3 = "Isn't there some way,",
        english_line4 = "Hidden from people's gaze,",
        english_line5 = 'That you can draw her to my side?',
        english_author = 'Fujiwara no Sadakata',

        japanese_line1 = '名にしおはば',
        japanese_line2 = '逢坂山の',
        japanese_line3 = 'さねかづら',
        japanese_line4 = '人にしられで',
        japanese_line5 = 'くるよしもがな',
        japanese_author = '三条右大臣',

        romaji_line1 = 'Na ni shi owaba',
        romaji_line2 = 'Osakayama no',
        romaji_line3 = 'Sanekazura',
        romaji_line4 = 'Hito ni shirarede',
        romaji_line5 = 'Kuru yoshi mo gana',
        romaji_author = 'Sanjo Udaijin',
    )
    card26 = karuta_cards(
        english_line1 = 'If the maple leaves',
        english_line2 = 'On Ogura mountain',
        english_line3 = 'Could only have hearts,',
        english_line4 = 'They would longingly await',
        english_line5 = "The emperor's pilgrimage.",
        english_author = 'Fujiwara no Tadahira',

        japanese_line1 = '小倉山',
        japanese_line2 = '峰のもみじ葉',
        japanese_line3 = '心あらば',
        japanese_line4 = '今ひとたびの',
        japanese_line5 = 'みゆきまたなむ',
        japanese_author = '貞信公',

        romaji_line1 = 'Ogurayama',
        romaji_line2 = 'Mine no momijiba',
        romaji_line3 = 'Kokoro araba',
        romaji_line4 = 'Ima hitotabi no',
        romaji_line5 = 'Miyuki matanan',
        romaji_author = 'Teishin Ko',
    )
    card27 = karuta_cards(
        english_line1 = "Over Mika's plain,",
        english_line2 = 'Gushing forth and flowing free,',
        english_line3 = "Is Izumi's stream.",
        english_line4 = 'I do not know if we have met:',
        english_line5 = 'Why, then, do I long for her?',
        english_author = 'Fujiwara no Kanesuke',

        japanese_line1 = 'みかの原',
        japanese_line2 = 'わきてながるる',
        japanese_line3 = '泉川',
        japanese_line4 = 'いつ見きとてか',
        japanese_line5 = '恋しかるらむ',
        japanese_author = '中納言兼輔',

        romaji_line1 = 'Mika no Hara',
        romaji_line2 = 'Wakite nagaruru',
        romaji_line3 = 'Izumi-gawa',
        romaji_line4 = 'Itsu mi kitote ka',
        romaji_line5 = 'Koishi karuran',
        romaji_author = 'Chunagon Kanesuke',
    )
    card28 = karuta_cards(
        english_line1 = 'Winter loneliness',
        english_line2 = 'In a mountain village grows',
        english_line3 = 'Only deeper, when',
        english_line4 = 'Guests are gone, and leaves and grass',
        english_line5 = 'Are withered: troubling thoughts.',
        english_author = 'Minamoto no Muneyuki',

        japanese_line1 = '山里は',
        japanese_line2 = '冬ぞさびしさ',
        japanese_line3 = 'まさりける',
        japanese_line4 = '人めも草も',
        japanese_line5 = 'かれぬとおもへば',
        japanese_author = '源宗于朝臣',

        romaji_line1 = 'Yama-zato wa',
        romaji_line2 = 'Fuyu zo sabishisa',
        romaji_line3 = 'Masari keru',
        romaji_line4 = 'Hitome mo kusa mo',
        romaji_line5 = 'Karenu to omoeba',
        romaji_author = 'Minamoto no Muneyuki Ason',
    )
    card29 = karuta_cards(
        english_line1 = 'If it were my wish',
        english_line2 = 'To pick the white chrysanthemums,',
        english_line3 = 'Puzzled by the frost',
        english_line4 = 'Of the early autumn time,',
        english_line5 = 'I by chance might pluck the flower.',
        english_author = 'Oshikochi no Mitsune',

        japanese_line1 = '心あてに',
        japanese_line2 = '折らばや折らむ',
        japanese_line3 = '初霜の',
        japanese_line4 = 'おきまどはせる',
        japanese_line5 = '白菊の花',
        japanese_author = '凡河内躬恒',

        romaji_line1 = 'Kokoroate ni',
        romaji_line2 = 'Orabaya oran',
        romaji_line3 = 'Hatsushimo no',
        romaji_line4 = 'Oki madowaseru',
        romaji_line5 = 'Shiragiku no hana',
        romaji_author = 'Oshikochi no Mitsune',
    )
    card30 = karuta_cards(
        english_line1 = 'Like the morning moon,',
        english_line2 = 'Cold, unpitying was my love.',
        english_line3 = 'And since we parted,',
        english_line4 = 'I dislike nothing so much',
        english_line5 = 'As the breaking light of day.',
        english_author = 'Mibu no Tadamine',

        japanese_line1 = '有明の',
        japanese_line2 = 'つれなくみえし',
        japanese_line3 = '別れより',
        japanese_line4 = '暁ばかり',
        japanese_line5 = 'うきものはなし',
        japanese_author = '壬生忠岑',

        romaji_line1 = 'Ariake no',
        romaji_line2 = 'Tsurenaku mieshi',
        romaji_line3 = 'Wakare yori',
        romaji_line4 = 'Akatsuki bakari',
        romaji_line5 = 'Uki mono wa nashi',
        romaji_author = 'Mibu no Tadamine',
    )
    card31 = karuta_cards(
        english_line1 = 'At the break of day,',
        english_line2 = 'Just as though the morning moon',
        english_line3 = 'Lightened the dim scene,',
        english_line4 = "Yoshino's village lay",
        english_line5 = 'In a haze of falling snow.',
        english_author = 'Sakanoue no Korenori',

        japanese_line1 = '朝ぼらけ',
        japanese_line2 = '有明の月と',
        japanese_line3 = 'みるまでに',
        japanese_line4 = '吉野の里に',
        japanese_line5 = 'ふれる白雪',
        japanese_author = '坂上是則',

        romaji_line1 = 'Asaborake',
        romaji_line2 = 'Ariake no tsuki to',
        romaji_line3 = 'Miru made ni',
        romaji_line4 = 'Yoshino no sato ni',
        romaji_line5 = 'Fureru shirayuki',
        romaji_author = 'Sakanoue no Korenori',
    )
    card32 = karuta_cards(
        english_line1 = 'In a mountain stream',
        english_line2 = 'There is a wattled barrier',
        english_line3 = 'Built by the busy wind.',
        english_line4 = "Yet it's only maple leaves,",
        english_line5 = 'Powerless to flow away.',
        english_author = 'Harumichi no Tsuraki',

        japanese_line1 = '山川に',
        japanese_line2 = '風のかけたる',
        japanese_line3 = 'しがらみは',
        japanese_line4 = '流れもあへぬ',
        japanese_line5 = '紅葉なりけり',
        japanese_author = '春道列樹',

        romaji_line1 = 'Yama kawa ni',
        romaji_line2 = 'Kaze no kaketaru',
        romaji_line3 = 'Shigarami wa',
        romaji_line4 = 'Nagare mo aenu',
        romaji_line5 = 'Momiji nari keri',
        romaji_author = 'Harumichi no Tsuraki',
    )
    card33 = karuta_cards(
        english_line1 = 'In the peaceful light',
        english_line2 = 'Of the ever-shining sun',
        english_line3 = 'In the days of spring,',
        english_line4 = "Why do the cherry's new-blown blooms",
        english_line5 = 'Scatter like restless thoughts?',
        english_author = 'Ki no Tomonori',

        japanese_line1 = '久方の',
        japanese_line2 = '光のどけき',
        japanese_line3 = '春の日に',
        japanese_line4 = 'しづ心なく',
        japanese_line5 = '花のちるらむ',
        japanese_author = '紀友則',

        romaji_line1 = 'Hisakata no',
        romaji_line2 = 'Hikari nodokeki',
        romaji_line3 = 'Haru no hi ni',
        romaji_line4 = 'Shizu-gokoro naku',
        romaji_line5 = 'Hana no chiruran',
        romaji_author = 'Ki no Tomonori',
    )
    card34 = karuta_cards(
        english_line1 = 'Who is still alive',
        english_line2 = 'When I have grown so old',
        english_line3 = 'That I can call my friends?',
        english_line4 = "Even Takasago's pines",
        english_line5 = 'No longer offer comfort.',
        english_author = 'Fujiwara no Okikaze',

        japanese_line1 = '誰をかも',
        japanese_line2 = '知る人にせむ',
        japanese_line3 = '高砂の',
        japanese_line4 = '松もむかしの',
        japanese_line5 = '友ならなくに',
        japanese_author = '藤原興風',

        romaji_line1 = 'Tare o ka mo',
        romaji_line2 = 'Shiru hito ni sen',
        romaji_line3 = 'Takasago no',
        romaji_line4 = 'Matsu mo mukashi no',
        romaji_line5 = 'Tomo nara naku ni',
        romaji_author = 'Fujiwara no Okikaze',
    )
    card35 = karuta_cards(
        english_line1 = 'The depths of the hearts',
        english_line2 = 'Of humankind cannot be known.',
        english_line3 = 'But in my birthplace',
        english_line4 = 'The plum blossoms smell the same',
        english_line5 = 'As in the years gone by.',
        english_author = 'Ki no Tsurayuki',

        japanese_line1 = '人はいさ',
        japanese_line2 = '心も知らず',
        japanese_line3 = 'ふるさとは',
        japanese_line4 = '花ぞむかしの',
        japanese_line5 = '香に匂ひける',
        japanese_author = '紀貫之',

        romaji_line1 = 'Hito wa isa',
        romaji_line2 = 'Kokoro mo shirazu',
        romaji_line3 = 'Furusato wa',
        romaji_line4 = 'Hana zo mukashi no',
        romaji_line5 = 'Ka ni nioi keru',
        romaji_author = 'Ki no Tsurayuki',
    )
    card36 = karuta_cards(
        english_line1 = 'In the summer night',
        english_line2 = 'The evening still seems present,',
        english_line3 = 'But the dawn is here.',
        english_line4 = 'To what region of the clouds',
        english_line5 = 'Has the wandering moon come home?',
        english_author = 'Kiyohara no Fukayabu',

        japanese_line1 = '夏の夜は',
        japanese_line2 = 'まだ宵ながら',
        japanese_line3 = '明けぬるを',
        japanese_line4 = '雲のいづくに',
        japanese_line5 = '月やどるらむ',
        japanese_author = '清原深養父',

        romaji_line1 = 'Natsu no yo wa',
        romaji_line2 = 'Mada yoi nagara',
        romaji_line3 = 'Akenuru o',
        romaji_line4 = 'Kumo no izuko ni',
        romaji_line5 = 'Tsuki yadoruran',
        romaji_author = 'Kiyohara no Fukayabu',
    )
    card37 = karuta_cards(
        english_line1 = 'In the autumn fields',
        english_line2 = 'When the heedless wind blows by',
        english_line3 = 'Over the pure-white dew,',
        english_line4 = 'How the myriad unstrung gems',
        english_line5 = 'Are scattered everywhere around',
        english_author = "Bun'ya no Asayasu",

        japanese_line1 = '白露を',
        japanese_line2 = '風のふきしく',
        japanese_line3 = '秋の野は',
        japanese_line4 = 'つらぬきとめぬ',
        japanese_line5 = '玉ぞちりける',
        japanese_author = '文屋朝康',

        romaji_line1 = 'Shiratsuyu o',
        romaji_line2 = 'Kaze no fukishiku',
        romaji_line3 = 'Aki no no wa',
        romaji_line4 = 'Tsuranuki tomenu',
        romaji_line5 = 'Tama zo chiri keru',
        romaji_author = "Fun'ya no Asayasu",
    )
    card38 = karuta_cards(
        english_line1 = 'Though he forsook me,',
        english_line2 = 'For myself I do not care:',
        english_line3 = 'He made a promise,',
        english_line4 = 'And his life, who is forsworn,',
        english_line5 = 'Oh how pitiful that is.',
        english_author = 'Lady Ukon',

        japanese_line1 = '忘らるる',
        japanese_line2 = '身をば思はず',
        japanese_line3 = '誓ひてし',
        japanese_line4 = '人の命の',
        japanese_line5 = '惜しくもあるかな',
        japanese_author = '右近',

        romaji_line1 = 'Wasuraruru',
        romaji_line2 = 'Mi o ba omowazu',
        romaji_line3 = 'Chikaite shi',
        romaji_line4 = 'Hito no inochi no',
        romaji_line5 = 'Oshiku mo aru kana',
        romaji_author = 'Ukon',
    )
    card39 = karuta_cards(
        english_line1 = 'Bamboo growing',
        english_line2 = 'Among the tangled reeds',
        english_line3 = 'Like my hidden love:',
        english_line4 = 'But it is too much to bear',
        english_line5 = 'That I still love her so.',
        english_author = 'Minamoto no Hitoshi',

        japanese_line1 = '浅茅生の',
        japanese_line2 = '小野の篠原',
        japanese_line3 = '忍ぶれど',
        japanese_line4 = 'あまりてなどか',
        japanese_line5 = '人の恋しき',
        japanese_author = '参議等',

        romaji_line1 = 'Asajiu no',
        romaji_line2 = 'Ono no shinohara',
        romaji_line3 = 'Shinoburedo',
        romaji_line4 = 'Amarite nado ka',
        romaji_line5 = 'Hito no koishiki',
        romaji_author = 'Sangi Hitoshi',
    )
    card40 = karuta_cards(
        english_line1 = 'Though I would hide it,',
        english_line2 = 'In my face it still appears--',
        english_line3 = 'My fond, secret love.',
        english_line4 = 'And now he questions me:',
        english_line5 = '"Is something bothering you?"',
        english_author = 'Taira no Kanemori',

        japanese_line1 = '忍ぶれど',
        japanese_line2 = '色に出でにけり',
        japanese_line3 = 'わが恋は',
        japanese_line4 = '物や思ふと',
        japanese_line5 = '人の問ふまで',
        japanese_author = '平兼盛',

        romaji_line1 = 'Shinoburedo',
        romaji_line2 = 'Iro ni ide ni keri',
        romaji_line3 = 'Waga koi wa',
        romaji_line4 = 'Mono ya omou to',
        romaji_line5 = 'Hito no tou made',
        romaji_author = 'Taira no Kanemori',
    )
    card41 = karuta_cards(
        english_line1 = 'It is true I love,',
        english_line2 = 'But the rumor of my love',
        english_line3 = 'Had gone far and wide,',
        english_line4 = 'When people should not have known',
        english_line5 = 'That I had begun to love.',
        english_author = 'Mibu no Tadami',

        japanese_line1 = '恋すてふ',
        japanese_line2 = '我が名はまだき',
        japanese_line3 = '立ちにけり',
        japanese_line4 = '人しれずこそ',
        japanese_line5 = '思ひそめしか',
        japanese_author = '壬生忠見',

        romaji_line1 = 'Koisu cho',
        romaji_line2 = 'Waga na wa madaki',
        romaji_line3 = 'Tachi ni keri',
        romaji_line4 = 'Hito shirezu koso',
        romaji_line5 = 'Omoi someshi ka',
        romaji_author = 'Mibu no Tadami',
    )
    card42 = karuta_cards(
        english_line1 = 'Our sleeves were wet with tears',
        english_line2 = 'As pledges that our love--',
        english_line3 = 'Will last until',
        english_line4 = "Over Sue's Mount of Pines",
        english_line5 = 'Ocean waves are breaking.',
        english_author = 'Kiyohara no Motosuke',

        japanese_line1 = 'ちぎりきな',
        japanese_line2 = 'かたみに袖を',
        japanese_line3 = 'しぼりつつ',
        japanese_line4 = '末の松山',
        japanese_line5 = '波こさじとは',
        japanese_author = '清原元輔',

        romaji_line1 = 'Chigiriki na',
        romaji_line2 = 'Katami ni sode o',
        romaji_line3 = 'Shibori tsutsu',
        romaji_line4 = 'Sue no Matsuyama',
        romaji_line5 = 'Nami kosaji to wa',
        romaji_author = 'Kiyohara no Motosuke',
    )
    card43 = karuta_cards(
        english_line1 = 'I have met my love.',
        english_line2 = 'When I compare this present',
        english_line3 = 'With feelings of the past,',
        english_line4 = 'My passion is now as if',
        english_line5 = 'I have never loved before.',
        english_author = 'Fujiwara no Atsutada',

        japanese_line1 = '逢ひ見ての',
        japanese_line2 = '後の心',
        japanese_line3 = 'くらぶれば',
        japanese_line4 = 'むかしは物を',
        japanese_line5 = '思はざりけり',
        japanese_author = '権中納言敦忠',

        romaji_line1 = 'Ai mite no',
        romaji_line2 = 'Nochi no kokoro ni',
        romaji_line3 = 'Kurabureba',
        romaji_line4 = 'Mukashi wa mono o',
        romaji_line5 = 'Omowazari keri',
        romaji_author = 'Gon Chunagon Atsutada',
    )
    card44 = karuta_cards(
        english_line1 = 'If it should happen',
        english_line2 = 'That we never met again,',
        english_line3 = 'I would not complain;',
        english_line4 = 'And I doubt that she or I',
        english_line5 = 'Would feel that we were left alone.',
        english_author = 'Fujiwara no Asatada',

        japanese_line1 = '逢ふことの',
        japanese_line2 = '絶えてしなくは',
        japanese_line3 = '中々に',
        japanese_line4 = '人をも身をも',
        japanese_line5 = '恨みざらまし',
        japanese_author = '中納言朝忠',

        romaji_line1 = 'Au koto no',
        romaji_line2 = 'Taete shi nakuwa',
        romaji_line3 = 'Nakanaka ni',
        romaji_line4 = 'Hito o mo mi o mo',
        romaji_line5 = 'Urami zaramashi',
        romaji_author = 'Chunagon Asatada',
    )
    card45 = karuta_cards(
        english_line1 = 'Surely there is none',
        english_line2 = 'Who will speak a pitying word',
        english_line3 = 'About my lost love.',
        english_line4 = "Now my folly's fitting end",
        english_line5 = 'Is my own nothingness.',
        english_author = 'Fujiwara no Koremasa',

        japanese_line1 = 'あはれとも',
        japanese_line2 = 'いふべき人は',
        japanese_line3 = '思ほえで',
        japanese_line4 = '身のいたづらに',
        japanese_line5 = 'なりぬべきかな',
        japanese_author = '謙徳公',

        romaji_line1 = 'Aware to mo',
        romaji_line2 = 'Iu beki hito wa',
        romaji_line3 = 'Omooede',
        romaji_line4 = 'Mi no itazura ni',
        romaji_line5 = 'Narinu beki kana',
        romaji_author = 'Kentoku Ko',
    )
    card46 = karuta_cards(
        english_line1 = 'Like a mariner',
        english_line2 = "Sailing over Yura's strait",
        english_line3 = 'With his rudder gone:',
        english_line4 = 'Where, over the deep of love,',
        english_line5 = 'The end lies, I do not know.',
        english_author = 'Sone no Yoshitada',

        japanese_line1 = '由良のとを',
        japanese_line2 = 'わたる舟人',
        japanese_line3 = 'かぢをたえ',
        japanese_line4 = '行く方もしらぬ',
        japanese_line5 = '恋の道かな',
        japanese_author = '曽禰好忠',

        romaji_line1 = 'Yura no to o',
        romaji_line2 = 'Wataru funabito',
        romaji_line3 = 'Kaji o tae',
        romaji_line4 = 'Yukue mo shiranu',
        romaji_line5 = 'Koi no michi kana',
        romaji_author = 'Sone no Yoshitada',
    )
    card47 = karuta_cards(
        english_line1 = 'To the dim cottage',
        english_line2 = 'Overgrown with thick-leaved vines',
        english_line3 = 'In its loneliness',
        english_line4 = 'Comes the dreary autumn time:',
        english_line5 = 'But there no people come.',
        english_author = 'The Monk Egyo',

        japanese_line1 = '八重むぐら',
        japanese_line2 = 'しげれる宿の',
        japanese_line3 = 'さびしきに',
        japanese_line4 = '人こそ見えね',
        japanese_line5 = '秋は来にけり',
        japanese_author = '恵慶法師',

        romaji_line1 = 'Yaemugura',
        romaji_line2 = 'Shigereru yado no',
        romaji_line3 = 'Sabishiki ni',
        romaji_line4 = 'Hito koso miene',
        romaji_line5 = 'Aki wa ki ni keri',
        romaji_author = 'Egyo Hoshi',
    )
    card48 = karuta_cards(
        english_line1 = 'Like a driven wave,',
        english_line2 = 'Dashed by fierce winds on a rock,',
        english_line3 = 'So am I: alone',
        english_line4 = 'And crushed upon the shore,',
        english_line5 = 'Remembering what has been.',
        english_author = 'Minamoto no Shigeyuki',

        japanese_line1 = '風をいたみ',
        japanese_line2 = '岩うつ波の',
        japanese_line3 = 'おのれのみ',
        japanese_line4 = 'くだけて物を',
        japanese_line5 = 'おもふ頃かな',
        japanese_author = '源重之',

        romaji_line1 = 'Kaze o itami',
        romaji_line2 = 'Iwa utsu nami no',
        romaji_line3 = 'Onore nomi',
        romaji_line4 = 'Kudakete mono o',
        romaji_line5 = 'Omou koro kana',
        romaji_author = 'Minamoto no Shigeyuki',
    )
    card49 = karuta_cards(
        english_line1 = "Like the guard's fires",
        english_line2 = 'Kept at the imperial gateway--',
        english_line3 = 'Burning through the night,',
        english_line4 = 'Dull in ashes through the day--',
        english_line5 = 'Is the love aglow in me.',
        english_author = 'Onakatomi no Yoshinobu Ason',

        japanese_line1 = 'みかき守',
        japanese_line2 = '衛士のたく火の',
        japanese_line3 = '夜はもえ',
        japanese_line4 = '昼は消えつつ',
        japanese_line5 = '物をこそおもへ',
        japanese_author = '大中臣能宣朝臣',

        romaji_line1 = 'Mikakimori',
        romaji_line2 = 'Eji no taku hi no',
        romaji_line3 = 'Yoru wa moe',
        romaji_line4 = 'Hiru wa kie tsutsu',
        romaji_line5 = 'Mono o koso omoe',
        romaji_author = 'Onakatomi no Yoshinobu Ason',
    )
    card50 = karuta_cards(
        english_line1 = 'For your precious sake,',
        english_line2 = 'Once my eager life itself',
        english_line3 = 'Was not dear to me.',
        english_line4 = "But now it is my heart's desire",
        english_line5 = 'It may long, long years endure.',
        english_author = 'Fujiwara no Yoshitaka',

        japanese_line1 = '君がため',
        japanese_line2 = '惜しからざりし',
        japanese_line3 = '命さへ',
        japanese_line4 = 'ながくもがなと',
        japanese_line5 = 'おもひけるかな',
        japanese_author = '藤原義孝',

        romaji_line1 = 'Kimi ga tame',
        romaji_line2 = 'Oshi karazarishi',
        romaji_line3 = 'Inochi sae',
        romaji_line4 = 'Nagaku mo gana to',
        romaji_line5 = 'Omoi keru kana',
        romaji_author = 'Fujiwara no Yoshitaka',
    )
    card51 = karuta_cards(
        english_line1 = 'How can I tell her',
        english_line2 = 'How fierce my love for her is?',
        english_line3 = 'Will she understand',
        english_line4 = 'That the love I feel for her',
        english_line5 = "Burns like Ibuki's fire plant?",
        english_author = 'Fujiwara no Sanekata',

        japanese_line1 = 'かくとだに',
        japanese_line2 = 'えやはいぶきの',
        japanese_line3 = 'さしも草',
        japanese_line4 = 'さしも知らじな',
        japanese_line5 = 'もゆる思ひを',
        japanese_author = '藤原実方朝臣',

        romaji_line1 = 'Kaku to dani',
        romaji_line2 = 'Eyawa ibuki no',
        romaji_line3 = 'Sashimogusa',
        romaji_line4 = 'Sashimo shiraji na',
        romaji_line5 = 'Moyuru omoi o',
        romaji_author = 'Fujiwara no Sanekata Ason',
    )
    card52 = karuta_cards(
        english_line1 = 'Though I know indeed',
        english_line2 = 'That the night will come again',
        english_line3 = 'After day has dawned,',
        english_line4 = 'Still, in truth, I hate the sight',
        english_line5 = "Of the morning's coming light.",
        english_author = 'Fujiwara no Michinobu',

        japanese_line1 = '明けぬれば',
        japanese_line2 = '暮るるものとは',
        japanese_line3 = '知りながら',
        japanese_line4 = 'なをうらめしき',
        japanese_line5 = 'あさぼらけかな',
        japanese_author = '藤原道信朝臣',

        romaji_line1 = 'Akenureba',
        romaji_line2 = 'Kururu mono to wa',
        romaji_line3 = 'Shiri nagara',
        romaji_line4 = 'Nao urameshiki',
        romaji_line5 = 'Asaborake kana',
        romaji_author = 'Fujiwara no Michinobu Ason',
    )
    card53 = karuta_cards(
        english_line1 = 'Lying all alone,',
        english_line2 = 'Through the hours of the night,',
        english_line3 = 'Till the daylight comes:',
        english_line4 = 'Can you realize at all',
        english_line5 = 'The emptiness of that night?',
        english_author = 'The Mother of Michitsuna',

        japanese_line1 = 'なげきつつ',
        japanese_line2 = 'ひとりぬる夜の',
        japanese_line3 = '明くる間は',
        japanese_line4 = 'いかに久しき',
        japanese_line5 = 'ものとかは知る',
        japanese_author = '右大将道綱母',

        romaji_line1 = 'Nageki tsutsu',
        romaji_line2 = 'Hitori nuru yo no',
        romaji_line3 = 'Akuru ma wa',
        romaji_line4 = 'Ikani hisashiki',
        romaji_line5 = 'Mono to ka wa shiru',
        romaji_author = 'Udaisho Michitsuna no Haha',
    )
    card54 = karuta_cards(
        english_line1 = 'If remembering me',
        english_line2 = 'Will for him in future years',
        english_line3 = 'Be too difficult,',
        english_line4 = 'It would be well this very day',
        english_line5 = 'That I should end my life.',
        english_author = 'The Mother of Gido Sanshi',

        japanese_line1 = '忘れじの',
        japanese_line2 = '行末までは',
        japanese_line3 = '難ければ',
        japanese_line4 = '今日を限りの',
        japanese_line5 = '命ともがな',
        japanese_author = '儀同三司母',

        romaji_line1 = 'Wasureji no',
        romaji_line2 = 'Yukusue made wa',
        romaji_line3 = 'Katakereba',
        romaji_line4 = 'Kyo o kagiri no',
        romaji_line5 = 'Inochi to mo gana',
        romaji_author = 'Gido Sanshi no Haha',
    )
    card55 = karuta_cards(
        english_line1 = 'Though the waterfall',
        english_line2 = 'Ceased its flowing long ago,',
        english_line3 = 'And its sound is stilled,',
        english_line4 = 'Yet, in name it ever flows,',
        english_line5 = 'And in fame may yet be heard.',
        english_author = 'Fujiwara no Kinto',

        japanese_line1 = '滝の音は',
        japanese_line2 = '絶えて久しく',
        japanese_line3 = 'なりぬれど',
        japanese_line4 = '名こそ流れて',
        japanese_line5 = 'なほ聞えけれ',
        japanese_author = '大納言公任',

        romaji_line1 = 'Taki no oto wa',
        romaji_line2 = 'Taete hisashiku',
        romaji_line3 = 'Narinuredo',
        romaji_line4 = 'Na koso nagarete',
        romaji_line5 = 'Nao kikoe kere',
        romaji_author = 'Dainagon Kinto',
    )
    card56 = karuta_cards(
        english_line1 = 'Soon my life will close.',
        english_line2 = 'When I am beyond this world',
        english_line3 = 'And have forgotten it,',
        english_line4 = 'Let me remember only this:',
        english_line5 = 'One final meeting with you.',
        english_author = 'Lady Izumi Shikibu',

        japanese_line1 = 'あらざらむ',
        japanese_line2 = 'この世の外の',
        japanese_line3 = '思ひ出に',
        japanese_line4 = '今ひとたびの',
        japanese_line5 = '逢ふこともがな',
        japanese_author = '和泉式部',

        romaji_line1 = 'Arazaran',
        romaji_line2 = 'Kono yo no hoka no',
        romaji_line3 = 'Omoide ni',
        romaji_line4 = 'Ima hitotabi no',
        romaji_line5 = 'Au koto mo gana',
        romaji_author = 'Izumi Shikibu',
    )
    card57 = karuta_cards(
        english_line1 = 'Meeting on the path:',
        english_line2 = 'But I cannot clearly know',
        english_line3 = 'If it was he,',
        english_line4 = 'Because the midnight moon',
        english_line5 = 'In a cloud had disappeared.',
        english_author = 'Lady Murasaki Shikibu',

        japanese_line1 = 'めぐりあひて',
        japanese_line2 = '見しやそれとも',
        japanese_line3 = 'わかぬ間に',
        japanese_line4 = '雲がくれにし',
        japanese_line5 = '夜半の月かげ',
        japanese_author = '紫式部',

        romaji_line1 = 'Meguri aite',
        romaji_line2 = 'Mishi ya sore to mo',
        romaji_line3 = 'Wakanu ma ni',
        romaji_line4 = 'Kumo-gakure ni shi',
        romaji_line5 = 'Yowa no tsuki kage',
        romaji_author = 'Murasaki Shikibu',
    )
    card58 = karuta_cards(
        english_line1 = 'As Mount Arima',
        english_line2 = 'Sends its rustling winds across',
        english_line3 = "Ina's bamboo plains,",
        english_line4 = 'I will be just as steadfast',
        english_line5 = 'And never will forget you.',
        english_author = 'Daini no Sanmi, Lady Kataiko',

        japanese_line1 = 'ありま山',
        japanese_line2 = '猪名の笹原',
        japanese_line3 = '風吹けば',
        japanese_line4 = 'いでそよ人を',
        japanese_line5 = '忘れやはする',
        japanese_author = '大弐三位',

        romaji_line1 = 'Arimayama',
        romaji_line2 = 'Ina no sasawara',
        romaji_line3 = 'Kaze fukeba',
        romaji_line4 = 'Ide soyo hito o',
        romaji_line5 = 'Wasure ya wa suru',
        romaji_author = 'Daini no Sanmi',
    )
    card59 = karuta_cards(
        english_line1 = 'Better to have slept',
        english_line2 = 'Care-free, than to keep vain watch',
        english_line3 = 'Through the passing night,',
        english_line4 = 'Till I saw the lonely moon',
        english_line5 = 'Traverse her descending path.',
        english_author = 'Lady Akazome Emon',

        japanese_line1 = 'やすらはで',
        japanese_line2 = '寝なまし物を',
        japanese_line3 = '小夜更けて',
        japanese_line4 = 'かたぶくまでの',
        japanese_line5 = '月を見しかな',
        japanese_author = '赤染衛門',

        romaji_line1 = 'Yasurawade',
        romaji_line2 = 'Nenamashi mono o',
        romaji_line3 = 'Sayo fukete',
        romaji_line4 = 'Katabuku made no',
        romaji_line5 = 'Tsuki o mishi kan',
        romaji_author = 'Akazome Emon',
    )
    card60 = karuta_cards(
        english_line1 = 'By Oe Mountain',
        english_line2 = 'The road to Ikuno',
        english_line3 = 'Is far away,',
        english_line4 = 'And neither have I beheld',
        english_line5 = 'Nor crossed its bridge of heaven.',
        english_author = 'Lady Koshikibu',

        japanese_line1 = '大江山',
        japanese_line2 = 'いく野の道の',
        japanese_line3 = 'とほければ',
        japanese_line4 = 'まだふみも見ず',
        japanese_line5 = '天の橋立',
        japanese_author = '小式部内侍',

        romaji_line1 = 'Oeyama',
        romaji_line2 = 'Ikuno no michi no',
        romaji_line3 = 'To kereba',
        romaji_line4 = 'Mada fumi mo mizu',
        romaji_line5 = 'Ama no Hashidate',
        romaji_author = 'Koshikibu no Naishi',
    )
    card61 = karuta_cards(
        english_line1 = 'Eight-fold cherry flowers',
        english_line2 = 'That at Nara--ancient seat',
        english_line3 = 'Of our state--have bloomed,',
        english_line4 = 'In our nine-fold palace court',
        english_line5 = 'Shed their sweet perfume today.',
        english_author = 'Lady Ise no Osuke',

        japanese_line1 = 'いにしへの',
        japanese_line2 = '奈良の都の',
        japanese_line3 = '八重桜',
        japanese_line4 = '今日九重に',
        japanese_line5 = '匂ひぬるかな',
        japanese_author = '伊勢大輔',

        romaji_line1 = 'Inishie no',
        romaji_line2 = 'Nara no miyako no',
        romaji_line3 = 'Yae-zakura',
        romaji_line4 = 'Kyo kokonoe ni',
        romaji_line5 = 'Nioi nuru kana',
        romaji_author = 'Ise no Osuke',
    )
    card62 = karuta_cards(
        english_line1 = "The rooster's crowing",
        english_line2 = 'In the middle of the night',
        english_line3 = 'Deceived the hearers;',
        english_line4 = "But at Osaka's gateway",
        english_line5 = 'The guards are never fooled.',
        english_author = 'Lady Sei Shonagon',

        japanese_line1 = '夜をこめて',
        japanese_line2 = '鳥の空音は',
        japanese_line3 = 'はかるとも',
        japanese_line4 = 'よにあふさかの',
        japanese_line5 = '関はゆるさじ',
        japanese_author = '清少納言',

        romaji_line1 = 'Yo o komete',
        romaji_line2 = 'Tori no sorane wa',
        romaji_line3 = 'Hakaru tomo',
        romaji_line4 = 'Yo ni Osaka no',
        romaji_line5 = 'Seki wa yurusaji',
        romaji_author = 'Sei Shonagon',
    )
    card63 = karuta_cards(
        english_line1 = 'Is there any way',
        english_line2 = 'Except by a messenger',
        english_line3 = 'To send these words to you?',
        english_line4 = "If I could, I'd come to you",
        english_line5 = 'To say goodbye forever.',
        english_author = 'Fujiwara no Michimasa',

        japanese_line1 = '今はただ',
        japanese_line2 = '思ひ絶えなむ',
        japanese_line3 = 'とばかりを',
        japanese_line4 = '人づてならで',
        japanese_line5 = 'いふよしもがな',
        japanese_author = '左京大夫道雅',

        romaji_line1 = 'Ima wa tada',
        romaji_line2 = 'Omoi taenan',
        romaji_line3 = 'To bakari wo',
        romaji_line4 = 'Hito-zute nara de',
        romaji_line5 = 'Iu yoshi mo gana',
        romaji_author = 'Sakyo no Daibu Michimasa',
    )
    card64 = karuta_cards(
        english_line1 = 'In the early dawn',
        english_line2 = 'When the mists on Uji River',
        english_line3 = 'Slowly lift and clear,',
        english_line4 = 'From the shallows to the deep,',
        english_line5 = 'The stakes of fishing nets appear.',
        english_author = 'Fujiwara no Sadayori',

        japanese_line1 = '朝ぼらけ',
        japanese_line2 = '宇治の川ぎり',
        japanese_line3 = 'たえだえに',
        japanese_line4 = 'あらはれわたる',
        japanese_line5 = 'ぜぜの網代木',
        japanese_author = '権中納言定頼',

        romaji_line1 = 'Asaborake',
        romaji_line2 = 'Uji no kawagiri',
        romaji_line3 = 'Tae-dae ni',
        romaji_line4 = 'Araware wataru',
        romaji_line5 = 'Zeze no ajirogi',
        romaji_author = 'GonChunagon Sadayori',
    )
    card65 = karuta_cards(
        english_line1 = 'Even when your hate',
        english_line2 = 'Makes me stain my sleeves with tears',
        english_line3 = 'In cold misery,',
        english_line4 = 'Worse than hate and misery',
        english_line5 = 'Is the loss of my good name.',
        english_author = 'Lady Sagami',

        japanese_line1 = '恨みわび',
        japanese_line2 = 'ほさぬ袖だに',
        japanese_line3 = 'あるものを',
        japanese_line4 = '恋に朽ちなん',
        japanese_line5 = '名こそ惜しけれ',
        japanese_author = '相模',

        romaji_line1 = 'Urami wabi',
        romaji_line2 = 'Hosanu sode da ni',
        romaji_line3 = 'Aru mono o',
        romaji_line4 = 'Koi ni kuchinan',
        romaji_line5 = 'Na koso oshi kere',
        romaji_author = 'Sagami',
    )
    card66 = karuta_cards(
        english_line1 = 'On a mountain slope,',
        english_line2 = 'Solitary, uncompanioned,',
        english_line3 = 'Stands a cherry tree.',
        english_line4 = 'Except for you, lonely friend,',
        english_line5 = 'To others I am unknown.',
        english_author = 'Abbot Gyoson',

        japanese_line1 = 'もろともに',
        japanese_line2 = '哀れと思へ',
        japanese_line3 = '山桜',
        japanese_line4 = '花より外に',
        japanese_line5 = '知る人もなし',
        japanese_author = '大僧正行尊',

        romaji_line1 = 'Morotomo ni',
        romaji_line2 = 'Aware to omoe',
        romaji_line3 = 'Yama-zakura',
        romaji_line4 = 'Hana yori hoka ni',
        romaji_line5 = 'Shiru hito mo nashi',
        romaji_author = 'Daisojo Gyoson',
    )
    card67 = karuta_cards(
        english_line1 = 'If I lay my head',
        english_line2 = 'Upon his arm in the dark',
        english_line3 = 'Of a short spring night,',
        english_line4 = 'This innocent dream pillow',
        english_line5 = 'Will be the death of my good name.',
        english_author = 'Lady Suo',

        japanese_line1 = '春の夜の',
        japanese_line2 = '夢ばかりなる',
        japanese_line3 = '手枕に',
        japanese_line4 = 'かひなく立たむ',
        japanese_line5 = '名こそ惜しけれ',
        japanese_author = '周防内侍',

        romaji_line1 = 'Haru no yo no',
        romaji_line2 = 'Yume bakari naru',
        romaji_line3 = 'Tamakura ni',
        romaji_line4 = 'Kainaku tatan',
        romaji_line5 = 'Na koso oshi kere',
        romaji_author = 'Suo no Naishi',
    )
    card68 = karuta_cards(
        english_line1 = 'Though I do not want',
        english_line2 = 'To live on in this floating world,',
        english_line3 = 'If I remain here,',
        english_line4 = 'Let me remember only',
        english_line5 = 'This midnight and this moonrise.',
        english_author = 'Emperor Sanjo',

        japanese_line1 = '心にも',
        japanese_line2 = 'あらで浮世に',
        japanese_line3 = 'ながらへば',
        japanese_line4 = '恋しかるべき',
        japanese_line5 = '夜半の月かな',
        japanese_author = '三条院',

        romaji_line1 = 'Kokoro ni mo',
        romaji_line2 = 'Arade ukiyo ni',
        romaji_line3 = 'Nagaraeba',
        romaji_line4 = 'Koishikaru beki',
        romaji_line5 = 'Yowa no tsuki kana',
        romaji_author = 'Sanjo In',
    )
    card69 = karuta_cards(
        english_line1 = "By the wind storm's blast",
        english_line2 = "From Mimuro's mountain slopes",
        english_line3 = 'Maples leaves are torn,',
        english_line4 = 'Which turn Tatsuta River',
        english_line5 = 'Into a rich brocade.',
        english_author = 'The Monk Noin',

        japanese_line1 = 'あらし吹く',
        japanese_line2 = '三室の山の',
        japanese_line3 = 'もみぢ葉は',
        japanese_line4 = '龍田の川の',
        japanese_line5 = 'にしきなりけり',
        japanese_author = '能因法師',

        romaji_line1 = 'Arashi fuku',
        romaji_line2 = 'Mimuro no yama no',
        romaji_line3 = 'Momijiba wa',
        romaji_line4 = 'Tatsuta no kawa no',
        romaji_line5 = 'Nishiki nari keri',
        romaji_author = 'Noin Hoshi',
    )
    card70 = karuta_cards(
        english_line1 = 'In my loneliness',
        english_line2 = 'I leave my little hut.',
        english_line3 = 'When I look around,',
        english_line4 = 'Everywhere it is the same:',
        english_line5 = 'One lone, darkening autumn eve.',
        english_author = 'The Monk Ryosen',

        japanese_line1 = '寂しさに',
        japanese_line2 = '宿を立出て',
        japanese_line3 = 'ながむれば',
        japanese_line4 = 'いづこもおなじ',
        japanese_line5 = '秋の夕暮',
        japanese_author = '良暹法師',

        romaji_line1 = 'Sabishisa ni',
        romaji_line2 = 'Yado o tachi idete',
        romaji_line3 = 'Nagamureba',
        romaji_line4 = 'Izuko mo onaji',
        romaji_line5 = 'Aki no yugure',
        romaji_author = 'Ryosen Hoshi',
    )
    card71 = karuta_cards(
        english_line1 = 'When the evening comes,',
        english_line2 = 'From the rice leaves at my gate,',
        english_line3 = 'Gentle knocks are heard,',
        english_line4 = 'And, into my round rush-hut,',
        english_line5 = "Enters autumn's roaming breeze.",
        english_author = 'Minamoto no Tsunenobu',

        japanese_line1 = '夕されば',
        japanese_line2 = '門田の稲葉',
        japanese_line3 = 'おとづれて',
        japanese_line4 = 'あしのまろやに',
        japanese_line5 = '秋風ぞふく',
        japanese_author = '大納言経信',

        romaji_line1 = 'Yu sareba',
        romaji_line2 = 'Kadota no inaba',
        romaji_line3 = 'Otozurete',
        romaji_line4 = 'Ashi no maroya ni',
        romaji_line5 = 'Akikaze zo fuku',
        romaji_author = 'Dainagon Tsunenobu',
    )
    card72 = karuta_cards(
        english_line1 = 'Famous are the waves',
        english_line2 = 'That break on Takashi beach',
        english_line3 = 'In noisy arrogance.',
        english_line4 = 'If I should go near that shore.',
        english_line5 = 'I would only wet my sleeves.',
        english_author = 'Lady Kii',

        japanese_line1 = '音にきく',
        japanese_line2 = '高師の浜の',
        japanese_line3 = 'あだ浪は',
        japanese_line4 = 'かけじや袖の',
        japanese_line5 = 'ぬれもこそすれ',
        japanese_author = '祐子内親王家紀伊',

        romaji_line1 = 'Oto ni kiku',
        romaji_line2 = 'Takashi no hama no',
        romaji_line3 = 'Adanami wa',
        romaji_line4 = 'Kakeji ya sode no',
        romaji_line5 = 'Nure mo koso sure',
        romaji_author = 'Yushi Naishinno-ke no Kii',
    )
    card73 = karuta_cards(
        english_line1 = 'On that far mountain',
        english_line2 = 'On the slope below the peak',
        english_line3 = 'Cherries are in flower.',
        english_line4 = 'Oh, let the mountain mists',
        english_line5 = 'Not arise to hide the scene.',
        english_author = 'Oe no Masafusa',

        japanese_line1 = '高砂の',
        japanese_line2 = '尾の上の桜',
        japanese_line3 = '咲きにけり',
        japanese_line4 = '外山の霞',
        japanese_line5 = 'たたずもあらなん',
        japanese_author = '権中納言匡房',

        romaji_line1 = 'Takasago no',
        romaji_line2 = 'Onoe no sakura',
        romaji_line3 = 'Saki ni keri',
        romaji_line4 = 'Toyama no kasumi',
        romaji_line5 = 'Tatazu mo aranan',
        romaji_author = 'GonChunagon Masafusa',
    )
    card74 = karuta_cards(
        english_line1 = 'It was not for this',
        english_line2 = 'I prayed at the holy shrine:',
        english_line3 = 'That she would become',
        english_line4 = 'As pitiless and as cold',
        english_line5 = "As the storms on Hase's hills.",
        english_author = 'Minamoto no Toshiyori',

        japanese_line1 = 'うかりける',
        japanese_line2 = '人をはつせの',
        japanese_line3 = '山おろしよ',
        japanese_line4 = 'はげしかれとは',
        japanese_line5 = '祈らぬものを',
        japanese_author = '源俊頼朝臣',

        romaji_line1 = 'Ukari keru',
        romaji_line2 = 'Hito o Hatsuse n',
        romaji_line3 = 'Yama oroshiyo',
        romaji_line4 = 'Hageshikare to wa',
        romaji_line5 = 'Inoranu mono o',
        romaji_author = 'Minamoto no Toshiyori Ason',
    )
    card75 = karuta_cards(
        english_line1 = 'As dew promises',
        english_line2 = 'New life to the thirsty plant,',
        english_line3 = 'So did your vow to me.',
        english_line4 = 'Yet the year has passed away,',
        english_line5 = 'And autumn has come again.',
        english_author = 'Fujiwara no Mototoshi',

        japanese_line1 = '契りをきし',
        japanese_line2 = 'させもが露を',
        japanese_line3 = '命にて',
        japanese_line4 = 'あはれことしの',
        japanese_line5 = '秋もいぬめり',
        japanese_author = '藤原基俊',

        romaji_line1 = 'Chigiri okishi',
        romaji_line2 = 'Sasemo ga tsuyu o',
        romaji_line3 = 'Inochi ni te',
        romaji_line4 = 'Aware kotoshi no',
        romaji_line5 = 'Aki mo inumeri',
        romaji_author = 'Fujiwara no Mototosh',
    )
    card76 = karuta_cards(
        english_line1 = 'Over the wide sea',
        english_line2 = 'As I sail and look around,',
        english_line3 = 'It appears to me',
        english_line4 = 'That the white waves, far away,',
        english_line5 = 'Are the ever shining sky.',
        english_author = 'Fujiwara no Tadamichi',

        japanese_line1 = 'わたの原',
        japanese_line2 = 'こぎ出でて見れば',
        japanese_line3 = '久方の',
        japanese_line4 = '雲井にまよふ',
        japanese_line5 = 'おきつしらなみ',
        japanese_author = '法性寺入道関白太政大臣',

        romaji_line1 = 'Wata no hara',
        romaji_line2 = 'Kogi idete mireba',
        romaji_line3 = 'Hisakata no',
        romaji_line4 = 'Kumoi ni mayoo',
        romaji_line5 = 'Okitsu shiranami',
        romaji_author = 'Hoshoji no Nyudo Kanpaku Dajodaijin',
    )
    card77 = karuta_cards(
        english_line1 = 'Though a swift stream is',
        english_line2 = 'Divided by a boulder',
        english_line3 = 'In its headlong flow,',
        english_line4 = 'Though divided, on it rushes,',
        english_line5 = 'And at last unites again.',
        english_author = 'Emperor Sutoku',

        japanese_line1 = '瀬をはやみ',
        japanese_line2 = '岩にせかるる',
        japanese_line3 = '滝川の',
        japanese_line4 = 'われても末に',
        japanese_line5 = '逢はむとぞ思ふ',
        japanese_author = '崇徳院御製',

        romaji_line1 = 'Se o hayami',
        romaji_line2 = 'Iwa ni sekaruru',
        romaji_line3 = 'Takigawa no',
        romaji_line4 = 'Warete mo sue ni',
        romaji_line5 = 'Awan to zo omou',
        romaji_author = 'Sutoku In',
    )
    card78 = karuta_cards(
        english_line1 = 'Guard of Suma Gate,',
        english_line2 = 'From your sleep, how many nights',
        english_line3 = 'Have you awakened',
        english_line4 = 'At the cries of sanderlings,',
        english_line5 = 'Flying from Awaji Island?',
        english_author = 'Minamoto no Kanemasa',

        japanese_line1 = '淡路島',
        japanese_line2 = 'かよふ千鳥の',
        japanese_line3 = 'なく声に',
        japanese_line4 = 'いくよねざめぬ',
        japanese_line5 = 'すまの関守',
        japanese_author = '源兼昌',

        romaji_line1 = 'Awaji shima',
        romaji_line2 = 'Kayou chidori no',
        romaji_line3 = 'Naku koe ni',
        romaji_line4 = 'Ikuyo nezamenu',
        romaji_line5 = 'Suma no sekimori',
        romaji_author = 'Minamoto no Kanemasa',
    )
    card79 = karuta_cards(
        english_line1 = 'See how clear and bright',
        english_line2 = 'Is the moonlight finding ways',
        english_line3 = 'Through the riven clouds',
        english_line4 = 'That, with drifting autumn wind,',
        english_line5 = 'Gracefully float in the sky.',
        english_author = 'Fujiwara no Akisuke',

        japanese_line1 = '秋風に',
        japanese_line2 = 'たなびく雲の',
        japanese_line3 = 'たえまより',
        japanese_line4 = 'もれ出づる月の',
        japanese_line5 = 'かげのさやけさ',
        japanese_author = '左京大夫顕輔',

        romaji_line1 = 'Akikaze ni',
        romaji_line2 = 'Tanabiku kumo no',
        romaji_line3 = 'Taema yori',
        romaji_line4 = 'More izuru tsuki no',
        romaji_line5 = 'Kage no sayakes',
        romaji_author = 'Sakyo no Daibu Akisuke',
    )
    card80 = karuta_cards(
        english_line1 = 'Is it forever',
        english_line2 = 'That he hopes our love will last?',
        english_line3 = 'He did not answer.',
        english_line4 = 'And now my daylight thoughts',
        english_line5 = 'Are as tangled as my black hair.',
        english_author = 'Lady Horikawa',

        japanese_line1 = '長からむ',
        japanese_line2 = '心もしらず',
        japanese_line3 = '黒髪の',
        japanese_line4 = 'みだれてけさは',
        japanese_line5 = '物をこそ思へ',
        japanese_author = '待賢門院堀河',

        romaji_line1 = 'Nagakaran',
        romaji_line2 = 'Kokoro mo shirazu',
        romaji_line3 = 'Kurokami no',
        romaji_line4 = 'Midarete kesa wa',
        romaji_line5 = 'Mono o koso omoe',
        romaji_author = 'Taiken Moin no Horikawa',
    )
    card81 = karuta_cards(
        english_line1 = 'When I turned my look',
        english_line2 = 'Toward the place where I had heard',
        english_line3 = "The cuckoo's call,",
        english_line4 = 'The only thing I found',
        english_line5 = 'Was the moon of early dawn.',
        english_author = 'Fujiwara no Sanesada',

        japanese_line1 = 'ほととぎす',
        japanese_line2 = '鳴きつる方を',
        japanese_line3 = '眺むれば',
        japanese_line4 = 'ただ有明の',
        japanese_line5 = '月ぞのこれる',
        japanese_author = '後徳大寺左大臣',

        romaji_line1 = 'Hototogisu',
        romaji_line2 = 'Nakitsuru kata o',
        romaji_line3 = 'Nagamureba',
        romaji_line4 = 'Tada ariake no',
        romaji_line5 = 'Tsuki zo nokoreru',
        romaji_author = 'Go Tokudaiji no Sadaijin',
    )
    card82 = karuta_cards(
        english_line1 = 'Though in deep distress',
        english_line2 = 'Through your cruel blow, my life',
        english_line3 = 'Still is left to me.',
        english_line4 = 'But I cannot keep my tears;',
        english_line5 = 'They break forth from my grief.',
        english_author = 'The Monk Doin',

        japanese_line1 = '思ひわび',
        japanese_line2 = 'さても命は',
        japanese_line3 = 'あるものを',
        japanese_line4 = '憂きに堪へぬは',
        japanese_line5 = 'なみだなりけり',
        japanese_author = '道因法師',

        romaji_line1 = 'Omoi wabi',
        romaji_line2 = 'Satemo inochi wa',
        romaji_line3 = 'Aru mono o',
        romaji_line4 = 'Uki ni taenu wa',
        romaji_line5 = 'Namida nari keri',
        romaji_author = 'Doin Hoshi',
    )
    card83 = karuta_cards(
        english_line1 = 'From this world I think',
        english_line2 = 'That there is nowhere to escape.',
        english_line3 = 'I wanted to hide',
        english_line4 = "In the mountains' farthest depths;",
        english_line5 = "But there I hear the stag's cry.",
        english_author = 'Fujiwara no Toshinari',

        japanese_line1 = '世の中よ',
        japanese_line2 = '道こそなけれ',
        japanese_line3 = '思ひ入る',
        japanese_line4 = '山のおくにも',
        japanese_line5 = '鹿ぞ鳴くなる',
        japanese_author = '皇太后宮大夫俊成',

        romaji_line1 = 'Yo no naka yo',
        romaji_line2 = 'Michi koso nakere',
        romaji_line3 = 'Omoi iru',
        romaji_line4 = 'Yama no oku ni mo',
        romaji_line5 = 'Shika zo naku naru',
        romaji_author = 'Kotaigogu no Daibu Toshinari',
    )
    card84 = karuta_cards(
        english_line1 = 'If I should live long,',
        english_line2 = 'Then perhaps the present days',
        english_line3 = 'May be dear to me,',
        english_line4 = 'Just as past time filled with grief',
        english_line5 = 'Comes quietly back in thought.',
        english_author = 'Fujiwara no Kiyosuke',

        japanese_line1 = 'ながらへば',
        japanese_line2 = 'またこの頃や',
        japanese_line3 = 'しのばれむ',
        japanese_line4 = '憂しと見し世ぞ',
        japanese_line5 = '今は恋しき',
        japanese_author = '藤原清輔朝臣',

        romaji_line1 = 'Nagaraeba',
        romaji_line2 = 'Mata konogoro ya',
        romaji_line3 = 'Shinobaren',
        romaji_line4 = 'Ushi to mishi yo zo',
        romaji_line5 = 'Ima wa koishiki',
        romaji_author = 'Fujiwara no Kiyosuke Ason',
    )
    card85 = karuta_cards(
        english_line1 = 'Through an unsleeping night',
        english_line2 = 'Longingly I pass the hours,',
        english_line3 = "While the day's dawn lags.",
        english_line4 = 'And now the bedroom shutters',
        english_line5 = 'Are keeping light and life from me.',
        english_author = "The Monk Shun'e",

        japanese_line1 = '夜もすがら',
        japanese_line2 = '物思ふ頃は',
        japanese_line3 = '明けやらぬ',
        japanese_line4 = 'ねやのひまさへ',
        japanese_line5 = 'つれなかりけり',
        japanese_author = '俊恵法師',

        romaji_line1 = 'Yo mo sugara',
        romaji_line2 = 'Mono omou koro wa',
        romaji_line3 = 'Ake yaranu',
        romaji_line4 = 'Neya no hima sae',
        romaji_line5 = 'Tsure nakari keri',
        romaji_author = 'Shun\'e Hoshi',
    )
    card86 = karuta_cards(
        english_line1 = 'Should I blame the moon',
        english_line2 = 'For bringing forth this sadness,',
        english_line3 = 'As if it pictured grief?',
        english_line4 = 'Lifting up my troubled face,',
        english_line5 = 'I regard it through my tears.',
        english_author = 'The Monk Saigyo',

        japanese_line1 = 'なげけとて',
        japanese_line2 = '月やは物を',
        japanese_line3 = '思はする',
        japanese_line4 = 'かこちがほなる',
        japanese_line5 = 'わがなみだかな',
        japanese_author = '西行法師',

        romaji_line1 = 'Nageke tote',
        romaji_line2 = 'Tsuki ya wa mono o',
        romaji_line3 = 'Omowasuru',
        romaji_line4 = 'Kakochi gao naru',
        romaji_line5 = 'Waga namida kana',
        romaji_author = 'Saigyo Hoshi',
    )
    card87 = karuta_cards(
        english_line1 = 'An autumn eve:',
        english_line2 = 'See the valley mists arise',
        english_line3 = 'Among the fir leaves',
        english_line4 = "That still hold the dripping wet",
        english_line5 = "Of the chill day's sudden showers.",
        english_author = 'The Monk Jakuren',

        japanese_line1 = 'むらさめの',
        japanese_line2 = '露もまだひぬ',
        japanese_line3 = 'まきの葉に',
        japanese_line4 = '霧立ちのぼる',
        japanese_line5 = '秋の夕暮',
        japanese_author = '寂蓮法師',

        romaji_line1 = 'Murasame no',
        romaji_line2 = 'Tsuyu mo mada hinu',
        romaji_line3 = 'Maki no ha ni',
        romaji_line4 = 'Kiri tachinoboru',
        romaji_line5 = 'Aki no yugure',
        romaji_author = 'Jakuren Hoshi',
    )
    card88 = karuta_cards(
        english_line1 = 'After one brief night--',
        english_line2 = 'Short as a piece of the reeds',
        english_line3 = 'Growing in Naniwa bay--',
        english_line4 = 'Must I forever long for him',
        english_line5 = 'With my whole heart, till life ends?',
        english_author = 'Attendant to Empress Koka',

        japanese_line1 = '難波江の',
        japanese_line2 = '芦のかりねの',
        japanese_line3 = '一夜ゆへ',
        japanese_line4 = '身をつくしてや',
        japanese_line5 = '恋わたるべき',
        japanese_author = '皇嘉門院別当',

        romaji_line1 = 'Naniwae no',
        romaji_line2 = 'Ashi no karine no',
        romaji_line3 = 'Hitoyo yue',
        romaji_line4 = 'Mi o tsukushite ya',
        romaji_line5 = 'Koi wataru beki',
        romaji_author = 'Koka Moin no Betto',
    )
    card89 = karuta_cards(
        english_line1 = 'Like a string of gems',
        english_line2 = 'Grown weak, my life will break now;',
        english_line3 = 'For if I live on,',
        english_line4 = 'All I do to hide my love',
        english_line5 = 'May at last grow weak and fail.',
        english_author = 'Princess Shokushi',

        japanese_line1 = '玉の緒よ',
        japanese_line2 = '絶えなば絶えね',
        japanese_line3 = 'ながらへば',
        japanese_line4 = 'しのぶることの',
        japanese_line5 = 'よはりもぞする',
        japanese_author = '式子内親王',

        romaji_line1 = 'Tama no o yo',
        romaji_line2 = 'Taenaba taene',
        romaji_line3 = 'Nagaraeba',
        romaji_line4 = 'Shinoburu koto no',
        romaji_line5 = 'Yowari mo zo suru',
        romaji_author = 'Shokushi Naishinno',
    )
    card90 = karuta_cards(
        english_line1='Let me show him these!',
        english_line2="Even the fishermen's sleeves",
        english_line3="On Ojima's shores,",
        english_line4='Though wet through and wet again,',
        english_line5='Do not so change their colors.',
        english_author='Attendant to Empress Inpu',

        japanese_line1='見せばやな',
        japanese_line2='雄島のあまの',
        japanese_line3='袖だにも',
        japanese_line4='ぬれにぞぬれし',
        japanese_line5='色はかはらず',
        japanese_author='殷富門院大輔',

        romaji_line1='Misebaya na',
        romaji_line2='Ojima no ama no',
        romaji_line3='Sode dani mo',
        romaji_line4='Nure ni zo nureshi',
        romaji_line5='Iro wa kawarazu',
        romaji_author='Inpu Moin no Taifu',
    )
    card91 = karuta_cards(
        english_line1='In my cold bed,',
        english_line2='Drawing close my folded quilt,',
        english_line3='I sleep alone,',
        english_line4='While all through the frosty night',
        english_line5="I hear a cricket's lonely sound.",
        english_author='Fujiwara no Yoshitsune',

        japanese_line1='きりぎりす',
        japanese_line2='鳴くや霜夜の',
        japanese_line3='さむしろに',
        japanese_line4='衣かたしき',
        japanese_line5='ひとりかも寝む',
        japanese_author='後京極摂政太政大臣',

        romaji_line1='Kirigirisu',
        romaji_line2='Naku ya shimo yo no',
        romaji_line3='Samushiro ni',
        romaji_line4='Koromo katashiki',
        romaji_line5='Hitori kamo nen',
        romaji_author='Go Kyogoku no Sessho Dajodaijin',
    )
    card92 = karuta_cards(
        english_line1='Like a rock at sea,',
        english_line2='At ebb-tide hidden from view,',
        english_line3='Is my tear-drenched sleeve:',
        english_line4='Never for a moment dry,',
        english_line5='And no one knows it is there.',
        english_author='Lady Sanuki',

        japanese_line1='わが袖は',
        japanese_line2='潮干に見えぬ',
        japanese_line3='沖の石の',
        japanese_line4='人こそしらね',
        japanese_line5='かはくまもなし',
        japanese_author='二条院讃岐',

        romaji_line1='Waga sode wa',
        romaji_line2='Shiohi ni mienu',
        romaji_line3='Oki no ishi no',
        romaji_line4='Hito koso shirane',
        romaji_line5='Kawaku ma mo nashi',
        romaji_author='Nijo In no Sanuki',
    )
    card93 = karuta_cards(
        english_line1='If only our world',
        english_line2='Could be always as it is!',
        english_line3='How moving the sight',
        english_line4='Of the little fishing boat',
        english_line5='Drawn by ropes along the bank.',
        english_author='Minamoto no Sanetomo',

        japanese_line1='世の中は',
        japanese_line2='つねにもがもな',
        japanese_line3='なぎさこぐ',
        japanese_line4='あまの小舟の',
        japanese_line5='綱手かなしも',
        japanese_author='鎌倉右大臣',

        romaji_line1='Yo no naka wa',
        romaji_line2='Tsune ni mo ga mo na',
        romaji_line3='Nagisa kogu',
        romaji_line4='Ama no obune no',
        romaji_line5='Tsuna de kanashi mo',
        romaji_author='Kamakura no Udaijin',
    )
    card94 = karuta_cards(
        english_line1='From Mount Yoshino',
        english_line2='Blows a chill, autumnal wind.',
        english_line3='In the deepening night',
        english_line4='The ancient village shivers:',
        english_line5='Sounds of beating cloth I hear.',
        english_author='Fujiwara no Masatsune',

        japanese_line1='みよし野の',
        japanese_line2='山の秋風',
        japanese_line3='さよふけて',
        japanese_line4='ふるさとさむく',
        japanese_line5='衣うつなり',
        japanese_author='参議雅経',

        romaji_line1='Miyoshino no',
        romaji_line2='Yama no akikaze',
        romaji_line3='Sayo fukete',
        romaji_line4='Furusato samuku',
        romaji_line5='Koromo utsu nari',
        romaji_author='Sangi Masatsune',
    )
    card95 = karuta_cards(
        english_line1='From the monastery',
        english_line2='On Mount Hiei I look out',
        english_line3='On this world of tears,',
        english_line4='And though I am unworthy,',
        english_line5='I shield it with my black sleeves.',
        english_author='Abbot Jien',

        japanese_line1='おほけなく',
        japanese_line2='うき世の民に',
        japanese_line3='おほふかな',
        japanese_line4='わがたつそまに',
        japanese_line5='墨染の袖',
        japanese_author='前大僧正慈円',

        romaji_line1='Okenaku',
        romaji_line2='Ukiyo no tami ni',
        romaji_line3='Ou kana',
        romaji_line4='Waga tatsu soma ni',
        romaji_line5='Sumizome no sode',
        romaji_author='Saki no Daisojo Jien',
    )
    card96 = karuta_cards(
        english_line1='Not the snow of flowers,',
        english_line2='That the hurrying wild wind whirls',
        english_line3='Round the garden court:',
        english_line4='What withers and falls away',
        english_line5='In this place is I myself.',
        english_author='Fujiwara no Kintsune',

        japanese_line1='花さそふ',
        japanese_line2='あらしの庭の',
        japanese_line3='雪ならで',
        japanese_line4='ふりゆくものは',
        japanese_line5='わが身なりけり',
        japanese_author='入道前太政大臣',

        romaji_line1='Hana sasou',
        romaji_line2='Arashi no niwa no',
        romaji_line3='Yuki nara de',
        romaji_line4='Furi yuku mono wa',
        romaji_line5='Waga mi nari keri',
        romaji_author='Nyudo Saki no Dajodaijin',
    )
    card97 = karuta_cards(
        english_line1='Like the salt sea-weed,',
        english_line2='Burning in the evening calm.',
        english_line3="On Matsuo's shore,",
        english_line4='All my being is aflame,',
        english_line5='Awaiting her who does not come.',
        english_author='Fujiwara no Sadaie, Fujiwara no Teika',

        japanese_line1='こぬ人を',
        japanese_line2='まつほの浦の',
        japanese_line3='夕なぎに',
        japanese_line4='やくやもしほの',
        japanese_line5='身もこがれつつ',
        japanese_author='権中納言定家',

        romaji_line1='Konu hito o',
        romaji_line2='Matsuho no ura no',
        romaji_line3='Yunagi ni',
        romaji_line4='Yaku ya moshio no',
        romaji_line5='Mi mo kogare tsutsu',
        romaji_author='GonChunagon Sadaie',
    )
    card98 = karuta_cards(
        english_line1="To Nara's brook comes",
        english_line2='Evening, and the rustling winds',
        english_line3="Stir the oak-trees' leaves.",
        english_line4='Not a sign of summer left',
        english_line5='But the sacred bathing there.',
        english_author='Fujiwara no Ietaka',

        japanese_line1='風そよぐ',
        japanese_line2='ならの小川の',
        japanese_line3='夕ぐれは',
        japanese_line4='みそぎぞ夏の',
        japanese_line5='しるしなりける',
        japanese_author='従二位家隆',

        romaji_line1='Kaze soyogu',
        romaji_line2='Nara no ogawa no',
        romaji_line3='Yugure wa',
        romaji_line4='Misogi zo natsu no',
        romaji_line5='Shirushi nari keru',
        romaji_author='Junii Ietaka',
    )
    card99 = karuta_cards(
        english_line1="For some men I grieve;",
        english_line2='Some men are hateful to me;',
        english_line3='And this wretched world',
        english_line4='To me, with all my sadness,',
        english_line5='Is a place of misery.',
        english_author='Emperor Gotoba',

        japanese_line1='人も惜し',
        japanese_line2='人も恨めし',
        japanese_line3='あぢきなく',
        japanese_line4='世を思ふゆゑに',
        japanese_line5='もの思ふ身は',
        japanese_author='後鳥羽院御製',

        romaji_line1='Hito mo oshi',
        romaji_line2='Hito mo urameshi',
        romaji_line3='Ajiki naku',
        romaji_line4='Yo o omou yue ni',
        romaji_line5='Mono omou mi wa',
        romaji_author='Gotoba In',
    )
    card100 = karuta_cards(
        english_line1="In this ancient house,",
        english_line2='Paved with a hundred stones,',
        english_line3='Ferns grow in the eaves;',
        english_line4='But numerous as they are,',
        english_line5='My old memories are more.',
        english_author='Emperor Juntoku',

        japanese_line1='百敷や',
        japanese_line2='古き軒端の',
        japanese_line3='しのぶにも',
        japanese_line4='なほあまりある',
        japanese_line5='むかしなりけり',
        japanese_author='順徳院御製',

        romaji_line1='Momoshiki ya',
        romaji_line2='Furuki nokiba no',
        romaji_line3='Shinobu ni mo',
        romaji_line4='Nao amari aru',
        romaji_line5='Mukashi nari keri',
        romaji_author='Juntoku In',
    )


    db.session.add(card1)
    db.session.add(card2)
    db.session.add(card3)
    db.session.add(card4)
    db.session.add(card5)
    db.session.add(card6)
    db.session.add(card7)
    db.session.add(card8)
    db.session.add(card9)
    db.session.add(card10)
    db.session.add(card11)
    db.session.add(card12)
    db.session.add(card13)
    db.session.add(card14)
    db.session.add(card15)
    db.session.add(card16)
    db.session.add(card17)
    db.session.add(card18)
    db.session.add(card19)
    db.session.add(card20)
    db.session.add(card21)
    db.session.add(card22)
    db.session.add(card23)
    db.session.add(card24)
    db.session.add(card25)
    db.session.add(card26)
    db.session.add(card27)
    db.session.add(card28)
    db.session.add(card29)
    db.session.add(card30)
    db.session.add(card31)
    db.session.add(card32)
    db.session.add(card33)
    db.session.add(card34)
    db.session.add(card35)
    db.session.add(card36)
    db.session.add(card37)
    db.session.add(card38)
    db.session.add(card39)
    db.session.add(card40)
    db.session.add(card41)
    db.session.add(card42)
    db.session.add(card43)
    db.session.add(card44)
    db.session.add(card45)
    db.session.add(card46)
    db.session.add(card47)
    db.session.add(card48)
    db.session.add(card49)
    db.session.add(card50)
    db.session.add(card51)
    db.session.add(card52)
    db.session.add(card53)
    db.session.add(card54)
    db.session.add(card55)
    db.session.add(card56)
    db.session.add(card57)
    db.session.add(card58)
    db.session.add(card59)
    db.session.add(card60)
    db.session.add(card61)
    db.session.add(card62)
    db.session.add(card63)
    db.session.add(card64)
    db.session.add(card65)
    db.session.add(card66)
    db.session.add(card67)
    db.session.add(card68)
    db.session.add(card69)
    db.session.add(card70)
    db.session.add(card71)
    db.session.add(card72)
    db.session.add(card73)
    db.session.add(card74)
    db.session.add(card75)
    db.session.add(card76)
    db.session.add(card77)
    db.session.add(card78)
    db.session.add(card79)
    db.session.add(card80)
    db.session.add(card81)
    db.session.add(card82)
    db.session.add(card83)
    db.session.add(card84)
    db.session.add(card85)
    db.session.add(card86)
    db.session.add(card87)
    db.session.add(card88)
    db.session.add(card89)
    db.session.add(card90)
    db.session.add(card91)
    db.session.add(card92)
    db.session.add(card93)
    db.session.add(card94)
    db.session.add(card95)
    db.session.add(card96)
    db.session.add(card97)
    db.session.add(card98)
    db.session.add(card99)
    db.session.add(card100)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_karuta_cards():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.karuta_cards RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM karuta_cards"))

    db.session.commit()
