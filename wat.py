import pcbnew
board = pcbnew.LoadBoard('main.kicad_pcb')
bcu = board.GetLayerID('B.Cu')
footprints = {footprint.GetReference(): footprint for footprint in board.GetFootprints()}
btracks = board.Tracks()

tracks = []
for i in range(4, 83):
    footprint = footprints[f'D{i}']
    x, y = footprint.GetPosition()
    track = pcbnew.PCB_TRACK(footprint.Pads()[1])
    track.SetLayer(bcu)
    track.SetWidth(250000)
    track.SetStart(pcbnew.wxPoint(x + 1400000, y))
    track.SetEnd(pcbnew.wxPoint(x + 9700000, y))
    tracks += [track]

for track in tracks:
    btracks.push_back(track)
board.Save('main.kicad_pcb')
