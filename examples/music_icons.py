"""
20 music-themed monochrome SVG icons.
Run: python3 icongen.py examples/music_icons.py --theme MusicMono
"""

build_theme(name="MusicMono", comment="Music app monochrome icons")

# ── Spotify ────────────────────────────────────────────────────────────────────
write("spotify", f"""
<circle cx="12" cy="12" r="9.5" {STROKE} stroke-width="{SW}"/>
<path d="M6.5 9 Q12 6.5 17.5 9"   {STROKE} stroke-width="{SWB}" {CAP}/>
<path d="M7.5 12.5 Q12 10.5 16.5 12.5" {STROKE} stroke-width="{SWB}" {CAP}/>
<path d="M8.5 16 Q12 14.5 15.5 16"     {STROKE} stroke-width="{SWB}" {CAP}/>
""")
link("spotify", "com.spotify.Client", "Spotify")

# ── Elisa (KDE music player) ───────────────────────────────────────────────────
write("org.kde.elisa", f"""
<circle cx="12" cy="12" r="9" {STROKE} stroke-width="{SW}"/>
<circle cx="12" cy="12" r="3" {STROKE} stroke-width="{SWS}"/>
<path d="M10 9 L16 12 L10 15Z" {FILL}/>
""")
link("org.kde.elisa", "elisa")

# ── Rhythmbox ─────────────────────────────────────────────────────────────────
write("rhythmbox", f"""
<path d="M5 13 Q5 4 12 4 Q19 4 19 13" {STROKE} stroke-width="{SWB}" {CAP}/>
<rect x="3"  y="12" width="4" height="6" rx="2" {FILL}/>
<rect x="17" y="12" width="4" height="6" rx="2" {FILL}/>
""")
link("rhythmbox", "org.gnome.Rhythmbox3", "headphones-app")

# ── VLC ────────────────────────────────────────────────────────────────────────
write("vlc", f"""
<path d="M12 2 L20 20 L4 20Z" {STROKE} stroke-width="{SW}" {CAP}/>
<line x1="7.8" y1="14" x2="16.2" y2="14" stroke="{C}" stroke-width="{SWB}" stroke-linecap="round"/>
<line x1="10"  y1="9"  x2="14"   y2="9"  stroke="{C}" stroke-width="{SWS}" stroke-linecap="round"/>
<line x1="3"   y1="20" x2="21"   y2="20" stroke="{C}" stroke-width="{SWB}" stroke-linecap="round"/>
""")
link("vlc", "org.videolan.vlc", "VLC")

# ── Generic music note ─────────────────────────────────────────────────────────
write("multimedia-player", f"""
<ellipse cx="7"  cy="17" rx="3"   ry="2.2" transform="rotate(-15 7 17)"  {FILL}/>
<ellipse cx="17" cy="15" rx="3"   ry="2.2" transform="rotate(-15 17 15)" {FILL}/>
<line x1="9.6"  y1="16.2" x2="9.6"  y2="7" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
<line x1="19.6" y1="14.2" x2="19.6" y2="5" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
<line x1="9.6"  y1="7"    x2="19.6" y2="5" stroke="{C}" stroke-width="{SWB}" stroke-linecap="round"/>
""")
link("multimedia-player", "audio-player", "media-player", "sound-player")

# ── Shortwave (internet radio) ────────────────────────────────────────────────
write("de.haeckerfelix.Shortwave", f"""
<line x1="12" y1="22" x2="12" y2="10" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
<path d="M12 22 L7 22 L10 14"  {STROKE} stroke-width="{SWS}" {CAP}/>
<path d="M12 22 L17 22 L14 14" {STROKE} stroke-width="{SWS}" {CAP}/>
<line x1="8.5"  y1="19" x2="15.5" y2="16" stroke="{C}" stroke-width="{SWS}" stroke-linecap="round" opacity="0.6"/>
<line x1="8.5"  y1="16" x2="15.5" y2="19" stroke="{C}" stroke-width="{SWS}" stroke-linecap="round" opacity="0.6"/>
<path d="M8 9.5 Q12 6.5 16 9.5"   {STROKE} stroke-width="{SW}"  {CAP}/>
<path d="M5.5 7 Q12 2.5 18.5 7"   {STROKE} stroke-width="{SWS}" {CAP}/>
<path d="M3 4.5 Q12 -1 21 4.5"    {STROKE} stroke-width="1.0"   {CAP} opacity="0.5"/>
""")
link("de.haeckerfelix.Shortwave", "shortwave", "internet-radio")

# ── Audacity ──────────────────────────────────────────────────────────────────
write("audacity", f"""
<rect x="2" y="3" width="20" height="18" rx="2" {STROKE} stroke-width="{SW}"/>
<path d="M4 12 Q6 6 8 12 Q10 18 12 12 Q14 6 16 12 Q18 18 20 12"
      {STROKE} stroke-width="{SW}" {CAP}/>
""")
link("audacity", "org.audacityteam.Audacity")

# ── Podcast / GNOME Podcasts ───────────────────────────────────────────────────
write("org.gnome.Podcasts", f"""
<circle cx="12" cy="12" r="4" {FILL}/>
<circle cx="12" cy="12" r="4" {STROKE} stroke-width="{SWS}"/>
<path d="M7 7 Q5 9.5 5 12 Q5 14.5 7 17"   {STROKE} stroke-width="{SW}" {CAP}/>
<path d="M17 7 Q19 9.5 19 12 Q19 14.5 17 17" {STROKE} stroke-width="{SW}" {CAP}/>
<path d="M4.5 4.5 Q1 8 1 12 Q1 16 4.5 19.5" {STROKE} stroke-width="{SWS}" {CAP}/>
<path d="M19.5 4.5 Q23 8 23 12 Q23 16 19.5 19.5" {STROKE} stroke-width="{SWS}" {CAP}/>
<line x1="12" y1="16" x2="12" y2="22" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
<line x1="9"  y1="22" x2="15" y2="22" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
""")
link("org.gnome.Podcasts", "gnome-podcasts", "podcast")

# ── Headphones (generic audio) ────────────────────────────────────────────────
write("audio-headphones", f"""
<path d="M4 14 Q4 5 12 5 Q20 5 20 14" {STROKE} stroke-width="{SWB}" {CAP}/>
<rect x="2"  y="13" width="4.5" height="6" rx="2.5" {FILL}/>
<rect x="17.5" y="13" width="4.5" height="6" rx="2.5" {FILL}/>
""")
link("audio-headphones", "headphones", "multimedia-player-audio")

# ── Equalizer / audio settings ────────────────────────────────────────────────
write("audio-equalizer", f"""
<line x1="4"  y1="20" x2="4"  y2="10" stroke="{C}" stroke-width="3" stroke-linecap="round"/>
<line x1="9"  y1="20" x2="9"  y2="5"  stroke="{C}" stroke-width="3" stroke-linecap="round"/>
<line x1="14" y1="20" x2="14" y2="13" stroke="{C}" stroke-width="3" stroke-linecap="round"/>
<line x1="19" y1="20" x2="19" y2="8"  stroke="{C}" stroke-width="3" stroke-linecap="round"/>
<circle cx="4"  cy="9"  r="2.5" {FILL}/>
<circle cx="9"  cy="4"  r="2.5" {FILL}/>
<circle cx="14" cy="12" r="2.5" {FILL}/>
<circle cx="19" cy="7"  r="2.5" {FILL}/>
""")
link("audio-equalizer", "equalizer", "multimedia-equalizer")

# ── mpv ───────────────────────────────────────────────────────────────────────
write("io.mpv.Mpv", f"""
<circle cx="12" cy="12" r="9.5" {STROKE} stroke-width="{SW}"/>
<path d="M9 7.5 L18 12 L9 16.5Z" {FILL}/>
""")
link("io.mpv.Mpv", "mpv", "multimedia-video-player", "media-video")

# ── GNOME Music ────────────────────────────────────────────────────────────────
write("org.gnome.Music", f"""
<circle cx="9"  cy="16" r="3" {STROKE} stroke-width="{SW}"/>
<circle cx="17" cy="14" r="3" {STROKE} stroke-width="{SW}"/>
<line x1="12" y1="16" x2="12" y2="7" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
<line x1="20" y1="14" x2="20" y2="5" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
<line x1="12" y1="7"  x2="20" y2="5" stroke="{C}" stroke-width="{SWB}" stroke-linecap="round"/>
""")
link("org.gnome.Music", "gnome-music")

# ── Lollypop ──────────────────────────────────────────────────────────────────
write("org.gnome.Lollypop", f"""
<circle cx="12" cy="12" r="9"  {STROKE} stroke-width="{SW}"/>
<circle cx="12" cy="12" r="5"  {STROKE} stroke-width="{SWS}"/>
<circle cx="12" cy="12" r="1.5" {FILL}/>
<path d="M12 3 L13 7 L12 7 L12 3Z" {FILL}/>
""")
link("org.gnome.Lollypop", "lollypop")

# ── Haruna video player ────────────────────────────────────────────────────────
write("org.kde.haruna", f"""
<rect x="2" y="4" width="20" height="16" rx="2" {STROKE} stroke-width="{SW}"/>
<path d="M10 9 L17 12 L10 15Z" {FILL}/>
<line x1="2"  y1="19" x2="22" y2="19" stroke="{C}" stroke-width="{SWS}"/>
<line x1="5"  y1="21" x2="8"  y2="21" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
<line x1="10" y1="21" x2="14" y2="21" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
<line x1="16" y1="21" x2="19" y2="21" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
""")
link("org.kde.haruna", "haruna")

# ── Clementine ────────────────────────────────────────────────────────────────
write("clementine", f"""
<path d="M12 3 Q17 3 20 7 Q23 11 21 16 Q19 21 14 22 Q9 23 5 19 Q1 15 3 9 Q5 3 12 3Z"
      {STROKE} stroke-width="{SW}"/>
<path d="M9 8 L15 12 L9 16Z" {FILL}/>
""")
link("clementine", "org.clementine_player.Clementine")

# ── Quod Libet ────────────────────────────────────────────────────────────────
write("quodlibet", f"""
<circle cx="7"  cy="17" r="2.8" {STROKE} stroke-width="{SW}"/>
<circle cx="17" cy="15" r="2.8" {STROKE} stroke-width="{SW}"/>
<line x1="9.8" y1="16.5" x2="9.8" y2="7"  stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
<line x1="19.8" y1="14.5" x2="19.8" y2="5" stroke="{C}" stroke-width="{SW}" stroke-linecap="round"/>
<line x1="9.8" y1="7" x2="19.8" y2="5" stroke="{C}" stroke-width="{SWB}" stroke-linecap="round"/>
<line x1="4"  y1="9"  x2="7"   y2="9"  stroke="{C}" stroke-width="{SWS}" stroke-linecap="round"/>
<line x1="4"  y1="12" x2="6.5" y2="12" stroke="{C}" stroke-width="{SWS}" stroke-linecap="round"/>
""")

# ── Strawberry music player ────────────────────────────────────────────────────
write("org.strawberrymusicplayer.strawberry", f"""
<path d="M12 21 Q5 16 5 10 Q5 5 9 4 Q11 3.5 12 5 Q13 3.5 15 4 Q19 5 19 10 Q19 16 12 21Z"
      {STROKE} stroke-width="{SW}" {CAP}/>
<path d="M12 5 Q12 8 10 10" {STROKE} stroke-width="{SWS}" {CAP}/>
""")
link("org.strawberrymusicplayer.strawberry", "strawberry")

# ── DeaDBeeF ──────────────────────────────────────────────────────────────────
write("deadbeef", f"""
<rect x="2" y="5" width="20" height="14" rx="2" {STROKE} stroke-width="{SW}"/>
<path d="M6 9 Q6 7 8 7 Q10 7 10 9 L10 15 Q10 17 8 17 Q6 17 6 15Z"
      {STROKE} stroke-width="{SWS}"/>
<path d="M13 7 L13 17 Q17 17 18 14 Q19 11 18 10 Q17 7 13 7Z"
      {STROKE} stroke-width="{SWS}"/>
""")

# ── JACK audio / PipeWire icon ────────────────────────────────────────────────
write("audio-card", f"""
<rect x="3" y="6" width="18" height="12" rx="2" {STROKE} stroke-width="{SW}"/>
<circle cx="8"  cy="12" r="2.5" {STROKE} stroke-width="{SWS}"/>
<circle cx="16" cy="12" r="2.5" {STROKE} stroke-width="{SWS}"/>
<rect x="6" y="3" width="2" height="3" rx="1" {FILL}/>
<rect x="11" y="3" width="2" height="3" rx="1" {FILL}/>
<rect x="16" y="3" width="2" height="3" rx="1" {FILL}/>
""")
link("audio-card", "multimedia-volume-control", "audio-volume-high")
