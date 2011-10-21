from Extended_Wave import Wave

def write_part(notes):
    '''Will write to the Wave class's array the line'''
    start_time = 0
    for i in notes:
        if i[1] != '':
            s.make_sine(start_time, i[0], i[1], 1000)
        start_time += i[0]
        if len(i) > 2:
            start_time += i[2]

def write_mozart_quintet(w):
    '''For each line of music, start a list. Append to that list tuples (note_length, note_name[, rest_after_note]). NOTE that 1 is 1 sec.'''
    #violin 1
    notes = []
    notes.append((1,'E5'))
    notes.append((1,'C#5'))
    notes.append((1,'B4'))
    notes.append((1,'A4'))
    notes.append((.5,'B4'))
    notes.append((.5,'C#5'))
    notes.append((.5,'D5'))
    notes.append((.5,'B4'))
    notes.append((1,'G#4'))
    notes.append((1,'A4'))
    notes.append((.5,'F#4'))
    notes.append((.5,'A4'))
    notes.append((.5,'E4'))
    notes.append((.5,'A4'))
    notes.append((1,'E4'))
    notes.append((.625,'D4'))
    notes.append((.1875,'C#4'))
    notes.append((.1875,'D4'))
    notes.append((.5,'C#4'))
    #End phrase 1 
    notes.append((1.5,''))
    notes.append((2,'G#4'))
    #Phrase 2
    notes.append((1,'E5'))
    notes.append((1,'C#5'))
    notes.append((1,'B4'))
    notes.append((1,'A4'))
    notes.append((.5,'B4'))
    notes.append((.5,'C#5'))
    notes.append((.5,'D5'))
    notes.append((.5,'F#5'))
    notes.append((1,'G#4'))
    notes.append((1,'A4'))
    notes.append((.5,'F#4'))
    notes.append((.5,'A4'))
    notes.append((.5,'E4'))
    notes.append((.5,'A4'))
    notes.append((1,'E4'))
    notes.append((.625,'D4'))
    notes.append((.1875,'C#4'))
    notes.append((.1875,'D4'))
    notes.append((.5,'C#4'))
    #End phrase 2
    notes.append((1.5,''))
    notes.append((2,'G#4'))
    #p3
    notes.append((.25,'A4'))
    notes.append((.25,'C#4'))
    notes.append((.25,'E4'))
    notes.append((.25,'A4'))
    notes.append((.25,'C#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'A5'))
    notes.append((.25,'C#6'))
    notes.append((.125,'B5'))
    notes.append((.125,'C#6'))
    notes.append((.125,'D6'))
    notes.append((.125,'C#6'))
    notes.append((.125,'D6'))
    notes.append((.125,'C#6'))
    notes.append((.125,'B5'))
    notes.append((.125,'A5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'A5'))
    notes.append((.125,'B5'))
    notes.append((.125,'A5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'E5'))
    notes.append((.125,'D5'))
    notes.append((.5,'C#5',1.5))
    #END P3
    #P4
    notes.append((1,'C#5'))
    notes.append((1,'B4'))
    notes.append((1,'A4'))
    notes.append((1,'G#4'))
    notes.append((1,'F#4'))
    notes.append((1,'E4'))
    notes.append((.5,'D4'))
    notes.append((.125,'G#4'))
    notes.append((.125,'F#4'))
    notes.append((.125,'G#4'))
    notes.append((.125,'A4'))
    notes.append((.5,'B4'))
    notes.append((.5,'A4'))
    notes.append((.125,'G#4'))
    notes.append((.125,'A4'))
    notes.append((.125,'B4'))
    notes.append((.125,'C#5'))
    notes.append((1,'D5'))
    notes.append((.5,'C#5'))
    notes.append((.5,'F#4'))
    notes.append((.5,'G#4'))
    notes.append((1,'A4'))
    notes.append((.5,'G#4',8.5))
    #END P4
    #P5
    notes.append((.25,'G#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'C5'))
    notes.append((.25,'C#5'))
    notes.append((.25,'F#5'))
    notes.append((.25,'D#5'))
    notes.append((.25,'A#4'))
    notes.append((.25,'B4'))
    notes.append((.25,'E5'))
    notes.append((.25,'C#5'))
    notes.append((.25,'G#4'))
    notes.append((.25,'A4'))
    notes.append((.25,'D#5'))
    notes.append((.25,'B4'))
    notes.append((.25,'G4'))
    notes.append((.25,'G#4'))
    notes.append((.25,'C#5'))
    notes.append((.25,'A4'))
    notes.append((.25,'F4'))
    notes.append((.25,'F#4'))
    
    notes.append((.375,'B4'))
    notes.append((.125,'G#4'))
    notes.append((.75,'B4'))
    notes.append((.25,'G#5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'E5'))
    notes.append((.125,'D#5'))
    notes.append((.125,'C#5'))
    notes.append((.25,'B4'))
    notes.append((.25,'A#4'))
    notes.append((.4,'A#4',.1))
    notes.append((.4,'A#4',.1))
    notes.append((.4,'A#4',.1))
    notes.append((.5,'B4',1.75))
    #p6
    notes.append((.125,'A4'))
    notes.append((.125,'G#4'))
    notes.append((.25,'C5'))
    notes.append((.25,'B4'))
    notes.append((.25,'A4'))
    notes.append((.25,'G4'))
    notes.append((.25,'F#4'))
    notes.append((.25,'E4'))
    notes.append((.5,'D#4',1.75))
    notes.append((.125,'A4'))
    notes.append((.125,'G#4'))
    notes.append((.25,'C5'))
    notes.append((.25,'B4'))
    notes.append((.25,'A4'))
    notes.append((.25,'G4'))
    notes.append((.25,'F#4'))
    notes.append((.25,'E4'))
    notes.append((.5,'D#4',.5))
    notes.append((.5,'A4',.5))
    notes.append((.5,'A4'))
    notes.append((.15,'D#5',.1))
    notes.append((.15,'D#5',.1))
    notes.append((.5,'D#5'))
    notes.append((.15,'F#5',.1))
    notes.append((.15,'F#5',.1))
    notes.append((.4,'F#5',.1))
    notes.append((.15,'A5',.1))
    notes.append((.15,'A5',.1))
    notes.append((.4,'A5',.1))
    

    write_part(notes)
    
    #violin 2
    notes = []
    notes.append((1,'C#5'))
    notes.append((1,'A4'))
    notes.append((1,'D4'))
    notes.append((1,'C#4'))
    notes.append((.5,'D4'))
    notes.append((.5,'E4'))
    notes.append((.5,'F#4'))
    notes.append((.5,'D4'))
    notes.append((1,'B3'))
    notes.append((1,'A3'))
    notes.append((.5,'A3',.5))
    notes.append((.5,'A3',.75))
    notes.append((.15,'A3',.1))
    notes.append((.15,'A3',.1))
    notes.append((.15,'A3',.35))
    notes.append((.15,'B3',.1))
    notes.append((.15,'B3',.1))
    notes.append((.15,'B3',.1))
    notes.append((.5,'C#4'))
    #End p1
    notes.append((1.5,''))
    notes.append((2,'B3'))
    #P2
    notes.append((1,'C#5'))
    notes.append((1,'A4'))
    notes.append((1,'D4'))
    notes.append((1,'C#4'))
    notes.append((.5,'F#4'))
    notes.append((.5,'A#4'))
    notes.append((.5,'B4'))
    notes.append((.5,'F#4'))
    notes.append((1,'E4'))
    notes.append((1,'E4'))
    notes.append((.5,'E4'))
    notes.append((1,'D4'))
    notes.append((.5,'C#4',.25))
    notes.append((.15,'C#4',.1))
    notes.append((.15,'C#4',.1))
    notes.append((.15,'C#4',.35))
    notes.append((.15,'B3',.1))
    notes.append((.15,'B3',.1))
    notes.append((.15,'B3',.1))
    notes.append((.5,'A3'))
    #End p2
    notes.append((1.5,''))
    notes.append((2,'B3'))
    #P3
    notes.append((.25,'C#4'))
    notes.append((.25,'A3'))
    notes.append((.25,'C#4'))
    notes.append((.25,'E4'))
    notes.append((.25,'A4'))
    notes.append((.25,'C#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'A5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'A5'))
    notes.append((.125,'B5'))
    notes.append((.125,'A5'))
    notes.append((.125,'B5'))
    notes.append((.125,'A5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'E5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'E5'))
    notes.append((.125,'D5'))
    notes.append((.125,'C#5'))
    notes.append((.125,'B4'))
    notes.append((.5,'A4',1.5))
    #END P3
    #P4
    notes.append((1,'A4'))
    notes.append((1,'G#4'))
    notes.append((1,'F#4'))
    notes.append((1,'E4'))
    notes.append((1,'D4'))
    notes.append((1,'C#4'))
    notes.append((.5,'B3',.5))
    notes.append((.5,'G#4'))
    notes.append((.5,'A4',.5))
    notes.append((.125,'D4'))
    notes.append((.125,'C#4'))
    notes.append((.125,'B3'))
    notes.append((.125,'A3'))
    notes.append((.5,'G#3'))
    notes.append((.5,'A3'))
    notes.append((.5,'B3'))
    notes.append((.5,'E4'))
    notes.append((.5,'A4'))
    notes.append((.5,'D#4'))
    notes.append((.5,'E4',1.5))
    #P5
    notes.append((1,'G#5'))
    notes.append((1,'F#5'))
    notes.append((1,'E5'))
    notes.append((1,'D#5'))
    notes.append((1,'C#5'))
    notes.append((1,'B4'))
    notes.append((1,'A4'))
    #P6
    notes.append((.25,''))
    notes.append((.15,'G#4',.1))
    notes.append((.15,'G#4',.1))
    notes.append((.15,'G#4',.1))
    notes.append((.25,''))
    notes.append((.15,'F#4',.1))
    notes.append((.15,'F#4',.1))
    notes.append((.15,'F#4',.1))
    notes.append((.25,''))
    notes.append((.15,'E4',.1))
    notes.append((.15,'E4',.1))
    notes.append((.15,'E4',.1))
    notes.append((.25,''))
    notes.append((.15,'D#4',.1))
    notes.append((.15,'D#4',.1))
    notes.append((.15,'D#4',.1))
    notes.append((.25,''))
    notes.append((.15,'C#4',.1))
    notes.append((.15,'C#4',.1))
    notes.append((.15,'C#4',.1))
    notes.append((.25,''))
    notes.append((.25,'B3'))
    notes.append((.25,'G#3'))
    notes.append((.25,'B3'))
    notes.append((.25,'G#3'))
    notes.append((.25,'B3'))
    notes.append((.25,'E4'))
    notes.append((.25,'G#4'))
    notes.append((.4,'C#4',.1))
    notes.append((.4,'C#4',.1))
    notes.append((.4,'C#4',.1))
    notes.append((.4,'C#4',.1))
    notes.append((.5,'B3',1.5))
    #P7
    notes.append((1.5,'E3'))
    notes.append((.25,'D#3'))
    notes.append((.25,'E3'))
    notes.append((.5,'F#3',1.5))
    notes.append((1.5,'E3'))
    notes.append((.25,'F#3'))
    notes.append((.25,'G3'))
    notes.append((.5,'A3',.5))
    notes.append((.5,'D#3',.5))
    notes.append((.5,'D#3'))
    notes.append((.15,'A3',.1))
    notes.append((.15,'A3',.1))
    notes.append((.5,'A3'))
    notes.append((.15,'D#4',.1))
    notes.append((.15,'D#4',.1))
    notes.append((.4,'D#4',.1))
    notes.append((.15,'F#4',.1))
    notes.append((.15,'F#4',.1))
    notes.append((.4,'F#4',.1))
    write_part(notes)

    #viola
    notes = []
    notes.append((1,'C#3'))
    notes.append((1,'E3'))
    notes.append((1,'G#3'))
    notes.append((1,'A3'))
    notes.append((.5,'F#3'))
    notes.append((.5,'E3'))
    notes.append((.5,'D3'))
    notes.append((.5,'F#3'))
    notes.append((1,'D4'))
    notes.append((1,'C#4'))
    notes.append((.5,'D4',.5))
    notes.append((.5,'E4',.75))
    notes.append((.15,'F#3',.1))
    notes.append((.15,'F#3',.1))
    notes.append((.15,'F#3',.35))
    notes.append((.15,'G#3',.1))
    notes.append((.15,'G#3',.1))
    notes.append((.15,'G#3',.1))
    notes.append((.5,'A3'))
    #End p1
    notes.append((1.5,''))
    notes.append((2,'E3'))
    #P2
    notes.append((1,'C#3'))
    notes.append((1,'E3'))
    notes.append((1,'G#3'))
    notes.append((1,'A3'))
    notes.append((.5,'D4'))
    notes.append((.5,'E4'))
    notes.append((.5,'F#4'))
    notes.append((.5,'D4'))
    notes.append((1,'B3'))
    notes.append((1,'A3'))
    notes.append((2,'A3',.25))
    notes.append((.15,'F#3',.1))
    notes.append((.15,'F#3',.1))
    notes.append((.15,'F#3',.35))
    notes.append((.15,'G#3',.1))
    notes.append((.15,'G#3',.1))
    notes.append((.15,'G#3',.1))
    notes.append((.5,'A3'))
    #End p2
    notes.append((1.5,''))
    notes.append((2,'E3'))
    notes.append((.5,'A3'))
    #P3
    notes.append((1.5,''))
    notes.append((2.5,'E4',15.5))
    #END P3
    #P4
    notes.append((1,'E5'))
    notes.append((1.5,'D#5'))
    notes.append((1,'C#5'))
    notes.append((1,'B4'))
    notes.append((1,'A4'))
    notes.append((1,'G#4'))
    notes.append((.5,'F#4'))
    #P5
    notes.append((.25,''))
    notes.append((.15,'E4',.1))
    notes.append((.15,'E4',.1))
    notes.append((.15,'E4',.1))
    notes.append((.25,''))
    notes.append((.15,'D#4',.1))
    notes.append((.15,'D#4',.1))
    notes.append((.15,'D#4',.1))
    notes.append((.25,''))
    notes.append((.15,'C#4',.1))
    notes.append((.15,'C#4',.1))
    notes.append((.15,'C#4',.1))
    notes.append((.25,''))
    notes.append((.15,'B3',.1))
    notes.append((.15,'B3',.1))
    notes.append((.15,'B3',.1))
    notes.append((.25,''))
    notes.append((.15,'A3',.1))
    notes.append((.15,'A3',.1))
    notes.append((.15,'A3',.1))
    notes.append((.25,''))
    notes.append((.25,'G#3'))
    notes.append((.25,'E3'))
    notes.append((.25,'G#3'))
    notes.append((.25,'E3'))
    notes.append((.25,'G#3'))
    notes.append((.25,'B3'))
    notes.append((.25,'E4'))
    notes.append((.4,'E3',.1))
    notes.append((.4,'E3',.1))
    notes.append((.4,'E3',.1))
    notes.append((.4,'E3',.1))
    notes.append((.5,'D#3',1.5))
    #P6
    notes.append((1.5,'E3'))
    notes.append((.25,'F#3'))
    notes.append((.25,'G3'))
    notes.append((.5,'A3',1.5))
    notes.append((1.5,'E3'))
    notes.append((.25,'D#3'))
    notes.append((.25,'E3'))
    notes.append((.5,'F#3',.5))
    notes.append((.5,'F#3',.5))
    notes.append((.5,'F#3'))
    notes.append((.15,'F#4',.1))
    notes.append((.15,'F#4',.1))
    notes.append((.5,'F#4'))
    notes.append((.15,'A4',.1))
    notes.append((.15,'A4',.1))
    notes.append((.4,'A4',.1))
    notes.append((.15,'D#5',.1))
    notes.append((.15,'D#5',.1))
    notes.append((.4,'D#5',.1))
    write_part(notes)

    #cello
    notes = []
    #P1
    notes.append((1,'A2'))
    notes.append((1,'C#3'))
    notes.append((1,'E3'))
    notes.append((1,'F#3'))
    notes.append((.5,'D3'))
    notes.append((.5,'C#3'))
    notes.append((.5,'B2'))
    notes.append((.5,'D3'))
    notes.append((1,'E3'))
    notes.append((1,'F#3'))
    notes.append((.5,'D3',.5))
    notes.append((.5,'C#3',.75))
    notes.append((.15,'B2',.1))
    notes.append((.15,'B2',.1))
    notes.append((.15,'B2',.35))
    notes.append((.15,'E3',.1))
    notes.append((.15,'E3',.1))
    notes.append((.15,'E3',.1))
    notes.append((.5,'A2'))
    #END P1
    notes.append((3.5,''))
    #P2
    notes.append((1,'A2'))
    notes.append((1,'C#3'))
    notes.append((1,'E3'))
    notes.append((1,'F#3'))
    notes.append((.5,'D3'))
    notes.append((.5,'C#3'))
    notes.append((.5,'B2'))
    notes.append((.5,'D3'))
    notes.append((1,'E3'))
    notes.append((1,'C#3'))
    notes.append((.5,'D3',.5))
    notes.append((.5,'A2',.75))
    notes.append((.15,'B2',.1))
    notes.append((.15,'B2',.1))
    notes.append((.15,'B2',.35))
    notes.append((.15,'E2',.1))
    notes.append((.15,'E2',.1))
    notes.append((.15,'E2',.1))
    notes.append((.5,'A2'))
    #END P2
    notes.append((3.5,''))
    #P3
    notes.append((2,''))
    notes.append((1.75,'E3'))
    notes.append((.125,'F#3'))
    notes.append((.125,'G#3'))
    notes.append((.5,'A3',13.75))
    #P4
    notes.append((.125,'E3'))
    notes.append((.125,'D#3'))
    notes.append((.25,'E3'))
    notes.append((.25,'F#3'))
    notes.append((.25,'G#3'))
    notes.append((.25,'A3'))
    notes.append((.25,'A#3'))
    notes.append((.25,'B3'))
    notes.append((.25,'C#4'))
    notes.append((.25,'B3'))
    notes.append((.25,'A#3'))
    notes.append((.25,'B3'))
    notes.append((.25,'A#3'))
    notes.append((.25,'B3'))
    notes.append((.25,'C#4'))
    notes.append((.25,'D#4'))
    
    notes.append((.25,'E4'))
    notes.append((.25,'C#4'))
    notes.append((.25,'G#3'))
    notes.append((.25,'A#3'))
    notes.append((.25,'D#4'))
    notes.append((.25,'B3'))
    notes.append((.25,'G3'))
    notes.append((.25,'A#3'))
    notes.append((.25,'C#4'))
    notes.append((.25,'A3'))
    notes.append((.25,'F3'))
    notes.append((.25,'F#3'))
    notes.append((.25,'B3'))
    notes.append((.25,'G#3'))
    notes.append((.25,'D#3'))
    notes.append((.25,'E3'))
    notes.append((.25,'A3'))
    notes.append((.25,'F#3'))
    notes.append((.25,'C#3'))
    notes.append((.25,'D#3'))
    notes.append((.5,'E3',.5))
    #P5
    notes.append((.5,'B2',.5))
    notes.append((.5,'C#3',.5))
    notes.append((.5,'G#2',.5))
    notes.append((.5,'A2',.5))
    notes.append((2,'E2'))
    notes.append((.4,'F#2',.1))
    notes.append((.4,'F#2',.1))
    notes.append((.4,'F#2',.1))
    notes.append((.4,'F#2',.1))
    notes.append((.5,'B2',1.5))
    
    #p6
    notes.append((2,'C3'))
    notes.append((.5,'B2',1.5))
    notes.append((2,'C2'))
    notes.append((.5,'B2',.5))
    notes.append((.5,'B2',.5))
    notes.append((.5,'B2',.5))
    notes.append((.5,'B3',.5))
    notes.append((.5,'B2',.5))
    notes.append((.5,'B3',.5))
    write_part(notes)

    #clarinet
    notes = []
    notes.append((12,'',.25))
    #P1
    notes.append((.25,'E3'))
    notes.append((.25,'A3'))
    notes.append((.25,'C#4'))
    notes.append((.25,'E4'))
    notes.append((.25,'A4'))
    notes.append((.25,'C#5'))
    notes.append((.25,'E5'))
    notes.append((.125,'D5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'D5'))
    notes.append((.125,'B4'))
    notes.append((.125,'G#4'))
    notes.append((.125,'B4'))
    notes.append((.125,'G#4'))
    notes.append((.125,'E4'))
    notes.append((.125,'D4'))
    notes.append((.125,'E4'))
    notes.append((.125,'D4'))
    notes.append((.125,'B3'))
    notes.append((.125,'G#3'))
    notes.append((.125,'B3'))
    notes.append((.125,'G#3'))
    notes.append((.125,'E3'))
    notes.append((.5,'A4'))
    #END P1
    notes.append((11.75,''))
    #P2
    notes.append((.25,'A3'))
    notes.append((.25,'C#4'))
    notes.append((.25,'E4'))
    notes.append((.25,'A4'))
    notes.append((.25,'C#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'A5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'B5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'E5'))
    notes.append((.125,'D5'))
    notes.append((.125,'E5'))
    notes.append((.125,'D5'))
    notes.append((.125,'B4'))
    notes.append((.125,'G#4'))
    notes.append((.125,'B4'))
    notes.append((.125,'G#4'))
    notes.append((.125,'E4'))
    notes.append((.125,'D4'))
    notes.append((.125,'E4'))
    notes.append((.125,'D4'))
    notes.append((.125,'B3'))
    notes.append((.5,'A3'))
    #END P2
    notes.append((3.75,''))
    #P3
    notes.append((.125,'A4'))
    notes.append((.125,'G#4'))
    notes.append((.25,'A4'))
    notes.append((.25,'B4'))
    notes.append((.25,'C#5'))
    notes.append((.25,'D5'))
    notes.append((.25,'D#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'F#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'D#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'D#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'F#5'))
    notes.append((.25,'G#5'))
    
    notes.append((.25,'A5'))
    notes.append((.25,'F#5'))
    notes.append((.25,'C#5'))
    notes.append((.25,'D5'))
    notes.append((.25,'G#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'C5'))
    notes.append((.25,'C#5'))
    notes.append((.25,'F#5'))
    notes.append((.25,'D5'))
    notes.append((.25,'A#4'))
    notes.append((.25,'B4'))
    notes.append((.25,'E5'))
    notes.append((.25,'C#5'))
    notes.append((.25,'G#4'))
    notes.append((.25,'A4'))
    
    notes.append((.125,'G#4'))
    notes.append((.125,'A4'))
    notes.append((.125,'B4'))
    notes.append((.125,'C#5'))
    notes.append((1,'D5'))
    notes.append((.5,'C#5'))
    notes.append((.125,'B4'))
    notes.append((.125,'C#5'))
    notes.append((.125,'D5'))
    notes.append((.125,'E5'))
    notes.append((1,'F#5'))
    notes.append((.5,'E5'))
    notes.append((.5,'D#5'))
    notes.append((.5,'D5'))
    notes.append((.5,'C#5'))
    notes.append((.5,'C5'))
    notes.append((.5,'B4',17.75))
    #P4
    notes.append((.125,'B4'))
    notes.append((.125,'A#4'))
    notes.append((.25,'B4'))
    notes.append((.25,'C#5'))
    notes.append((.25,'D#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'F#5'))
    notes.append((.25,'G#5'))
    notes.append((2,'A5',.25))
    
    notes.append((.125,'B4'))
    notes.append((.125,'A#4'))
    notes.append((.25,'B4'))
    notes.append((.25,'C#5'))
    notes.append((.25,'D#5'))
    notes.append((.25,'E5'))
    notes.append((.25,'F#5'))
    notes.append((.25,'G#5'))
    notes.append((2,'A5'))
    
    notes.append((.125,'A5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'E5'))
    notes.append((.125,'D#5'))
    notes.append((.125,'E5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'A5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'E5'))
    notes.append((.125,'D#5'))
    notes.append((.125,'E5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'G#5'))
    notes.append((.25,'A5'))
    notes.append((.125,'G#5'))
    notes.append((.125,'F#5'))
    notes.append((.125,'E5'))
    notes.append((.125,'D#5'))
    notes.append((.125,'C#5'))
    notes.append((.125,'B4'))
    notes.append((.25,'A4'))
    notes.append((.125,'G#4'))
    notes.append((.125,'F#4'))
    notes.append((.125,'E4'))
    notes.append((.125,'D#4'))
    notes.append((.125,'C#4'))
    notes.append((.125,'B3'))
    notes.append((.25,'A3'))
    notes.append((.125,'B3'))
    notes.append((.125,'C#4'))
    notes.append((.125,'D#4'))
    notes.append((.125,'E4'))
    notes.append((.125,'F#4'))
    notes.append((.125,'G#4'))
    notes.append((.5,'A4'))

    write_part(notes)
    
    

if __name__ == '__main__':
    '''Use this format!'''
    s = Wave()
    write_mozart_quintet(s)
    s.save()
