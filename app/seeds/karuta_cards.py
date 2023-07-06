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






    db.session.add(card1)
    db.session.add(card2)
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
