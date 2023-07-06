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
