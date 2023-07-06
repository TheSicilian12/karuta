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
