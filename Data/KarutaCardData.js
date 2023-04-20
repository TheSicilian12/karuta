cards = {
    0: {
        'english': {
            'yomifuda':{
                'firstLine': 'Coarse the rush-mat roof',
                'secondLine': 'Sheltering the harvest-hut',
                'thirdLine': 'Of the autumn rice-field;',
            },
            'torifuda': {
                'firstLine': 'And my sleeves are growing wet',
                'secondLine': 'With the moisture dripping through.'
            }
        },
        'japanese': {
            'yomifuda':{
                'firstLine': '秋の田の',
                'secondLine': 'かりほの庵の',
                'thirdLine': '苫をあらみ',
            },
            'torifuda': {
                'firstLine': 'わが衣手は',
                'secondLine': '露にぬれつつ'
            }
        },
        'romaji': {
            'yomifuda':{
                'firstLine': 'Aki no ta no',
                'secondLine': 'Kariho no io no',
                'thirdLine': 'Toma o arami',
            },
            'torifuda': {
                'firstLine': 'Waga koromode wa',
                'secondLine': 'Tsuyu ni nure tsutsu'
            }
        },
        'cardData': {
            'author': {
                'english': 'Emperor Tenchi',
                'japanese': '天智天皇',
                'romaji': 'Tenchi Tenno'
            }
        }
    },
    'citations': {
        'webSourceUrl': 'https://jti.lib.virginia.edu/japanese/hyakunin/index.html',
        'organization': 'The University of Virginia Library Electronic Text Center and the University of Pittsburgh East Asian Library'
    }
}
// currently language -> yomifuda -> text
// think about adjusting structure to be yomifuda -> language -> language text, I think this one makes more sense with data flow. Select the type of text you want then select the language.
