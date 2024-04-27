def translate_data(data):
    return {
        'status': 'sukces' if data['status'] == 'success' else 'błąd',
        'dane': {
            'miasto': data['data']['city'],
            'województwo': data['data']['state'],
            'kraj': data['data']['country'],
            'lokalizacja': {
                'typ': 'Punkt',
                'współrzędne': data['data']['location']['coordinates']
            },
            'aktualne': {
                'zanieczyszczenie': {
                    'czas': data['data']['current']['pollution']['ts'],
                    'jakość_powietrza_wg_US': data['data']['current']['pollution']['aqius'],
                    'główne_zanieczyszczenie_wg_US': data['data']['current']['pollution']['mainus'],
                    'jakość_powietrza_wg_Chin': data['data']['current']['pollution']['aqicn'],
                    'główny_zanieczyszcznie_wg_Chin': data['data']['current']['pollution']['maincn'],
                },
                'pogoda': {
                    'czas': data['data']['current']['weather']['ts'],
                    'temperatura': data['data']['current']['weather']['tp'],
                    'ciśnienie': data['data']['current']['weather']['pr'],
                    'wilgotność': data['data']['current']['weather']['hu'],
                    'prędkość_wiatru': data['data']['current']['weather']['ws'],
                    'kierunek_wiatru': data['data']['current']['weather']['wd'],
                }
            }
        }
    }
