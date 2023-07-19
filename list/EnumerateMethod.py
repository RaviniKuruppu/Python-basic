text = [’The’, ’main’, ’functional’, ’components’,
’of’, ’a’, ’mechanical’, ’ventilator’, ’are’,
’pressurized air inlet,’, ’pressurized oxygen inlet,’,
’gas blender,’, ’flow regulator,’, ’humidifier,’,
’control circuit,’, ’pressure regulator,’,
’inspiratory line,’, ’expiratory line,’, ’valves,’,
’pressure pump,’, ’filters’]

enumerated = enumerate(text,-8)
print('Enumerated text:')
for s in enumerated:
    print(s)