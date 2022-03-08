ticker = 'aapl'
gay = 'gay'
for i in range(0,10):
    with open ('test.txt','a') as f:
        f.write(f'{ticker} - {gay} - {i},\n')
        print('success')
