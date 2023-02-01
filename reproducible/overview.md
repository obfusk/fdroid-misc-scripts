Publishing apps with Reproducible Builds: https://f-droid.org/docs/Reproducible_Builds/  
Verification builds: https://f-droid.org/docs/Verification_Server/  
Scripts and data: https://github.com/obfusk/fdroid-misc-scripts  
Last updated: 2023-02-01

### Signatures in metadata: publishing both (upstream) developer-signed and F-Droid-signed APKs

#### {2022-{11,12},2023-{01,02}}-01: 6 apps

All apps (includes 1 no longer RB, making 7):

<details>

```
de.schildbach.wallet
de.schildbach.wallet_test
dev.obfusk.jiten
dev.obfusk.jiten_webview
dev.obfusk.sokobang
org.schabi.newpipe [no longer RB]
org.torproject.torservices
```

</details>

### Binaries: exclusively publishing (upstream) developer-signed APKs

#### 2022-11-01: 14 apps

All apps (includes 1 missing and 1 disabled, making 16):

<details>

```
androdns.android.leetdreams.ch.androdns
ch.admin.bag.covidcertificate.verifier
ch.admin.bag.covidcertificate.wallet
com.markuspage.android.certtools [missing]
com.mishiranu.dashchan
de.corona.tracing
de.schildbach.oeffi
eu.bubu1.fdroidclassic
info.guardianproject.checkey
nya.kitsunyan.foxydroid
org.briarproject.briar.android
org.jellyfin.androidtv [disabled]
org.jellyfin.mobile
rs.ltt.android
top.fumiama.copymanga
uk.co.keepawayfromfire.screens
```

</details>

#### 2022-12-01: 25 apps (+ 11)

Newly added (none were removed):

<details>

```
com.dhaval.bookland
com.github.bmx666.appcachecleaner [signflinger]
com.rafapps.earthviewformuzei [signflinger]
com.zionhuang.music
dev.yashgarg.qbit
io.github.project_kaat.gpsdrelay
io.github.quillpad [signflinger]
me.gloeckl.fallasleep
me.mudkip.moememos
org.joinmastodon.android [signflinger]
ru.ikkui.achie
```

</details>

Signed with [`signflinger`](https://github.com/obfusk/apksigcopier#what-about-apks-signed-by-gradlezipflingersignflinger-instead-of-apksigner): 4 apps.

#### 2023-01-01: 41 apps (+ 16)

Newly added (none were removed):

<details>

```
app.mlauncher
com.akshayaap.mouseremote [signflinger]
com.artikus.nolauncher [signflinger]
com.dosse.clock31 [signflinger]
com.eurokonverter [signflinger]
com.github.cvzi.wallpaperexport [signflinger]
com.jroddev.android_oss_release_tracker
com.martinmimigames.tinymusicplayer [signflinger]
de.niendo.ImapNotes3
dev.bartuzen.qbitcontroller [signflinger]
eu.auct.twitter2nitter [signflinger]
nl.tsmeets.todotree
org.afrikalan.tuxmath
org.asafonov.blockbuster
org.asafonov.monly
org.greatfire.wikiunblocked.fdroid [signflinger]
```

</details>

Signed with [`signflinger`](https://github.com/obfusk/apksigcopier#what-about-apks-signed-by-gradlezipflingersignflinger-instead-of-apksigner): 14 apps.

#### 2023-02-01: 54 apps (+ 13)

Newly added (none were removed):

<details>

```
InfinityLoop1309.NewPipeEnhanced [signflinger]
com.akansh.fileserversuit [signflinger]
com.nima.demomusix [signflinger]
com.nima.taskmanager
com.nima.wikianime [signflinger]
com.paranoiaworks.unicus.android.sse [signflinger]
com.razeeman.util.simpletimetracker [signflinger]
com.starry.myne
de.andicodes.vergissnix
deltazero.amarok.foss
io.github.yamin8000.dooz [signflinger]
org.localsend.localsend_app [signflinger]
yetzio.yetcalc [signflinger]
```

</details>

Signed with [`signflinger`](https://github.com/obfusk/apksigcopier#what-about-apks-signed-by-gradlezipflingersignflinger-instead-of-apksigner): 23 apps.

---

Total number of apps using RB: 6 + 54 = 60.
