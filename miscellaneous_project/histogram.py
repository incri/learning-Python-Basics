def histogram( value ):
    for n in value:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([7, 6, 5, 4, 3, 2, 7, 2, 3, 4, 5, 6, 7])
