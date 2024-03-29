# Overview of F-Droid apps published with Reproducible Builds

Publishing apps with Reproducible Builds: https://f-droid.org/docs/Reproducible_Builds/  
Verification builds: https://f-droid.org/docs/Verification_Server/  
Scripts and data: https://github.com/obfusk/fdroid-misc-scripts  
Last updated: 2023-10-03

![rb](../graphs/rb.png)

Description: graph "Apps published with Reproducible Builds (all)",
showing an almost straight line from 20 apps on 2022-11-01 to 199 apps
on 2023-10-01.

&rarr; [All F-Droid apps published with Reproducible Builds (2023-10-01)](2023-10-01-all.md)

### Signatures in metadata: publishing both (upstream) developer-signed and F-Droid-signed APKs

#### {2022-{11,12},2023-{01,02,03,04}}-01: 6 apps

All apps (includes 1 no longer RB, making 7):

<details>

* [`de.schildbach.wallet`](https://f-droid.org/packages/de.schildbach.wallet)
* [`de.schildbach.wallet_test`](https://f-droid.org/packages/de.schildbach.wallet_test)
* [`dev.obfusk.jiten`](https://f-droid.org/packages/dev.obfusk.jiten)
* [`dev.obfusk.jiten_webview`](https://f-droid.org/packages/dev.obfusk.jiten_webview)
* [`dev.obfusk.sokobang`](https://f-droid.org/packages/dev.obfusk.sokobang)
* [`org.schabi.newpipe`](https://f-droid.org/packages/org.schabi.newpipe) [no longer RB]
* [`org.torproject.torservices`](https://f-droid.org/packages/org.torproject.torservices)

</details>

#### 2023-{05,06,07,08,09}-01: 7 apps

All apps (NewPipe is RB again, making 7):

<details>

* [`de.schildbach.wallet`](https://f-droid.org/packages/de.schildbach.wallet)
* [`de.schildbach.wallet_test`](https://f-droid.org/packages/de.schildbach.wallet_test)
* [`dev.obfusk.jiten`](https://f-droid.org/packages/dev.obfusk.jiten)
* [`dev.obfusk.jiten_webview`](https://f-droid.org/packages/dev.obfusk.jiten_webview)
* [`dev.obfusk.sokobang`](https://f-droid.org/packages/dev.obfusk.sokobang)
* [`org.schabi.newpipe`](https://f-droid.org/packages/org.schabi.newpipe)
* [`org.torproject.torservices`](https://f-droid.org/packages/org.torproject.torservices)

</details>

#### 2023-10-01: 8 apps (+ 1)

Switched to RB:

<details>

* [`de.marmaro.krt.ffupdater`](https://f-droid.org/packages/de.marmaro.krt.ffupdater)

</details>

### Binaries: exclusively publishing (upstream) developer-signed APKs

#### 2022-11-01: 14 apps

All apps (includes 1 missing and 1 disabled, making 16):

<details>

* [`androdns.android.leetdreams.ch.androdns`](https://f-droid.org/packages/androdns.android.leetdreams.ch.androdns)
* [`ch.admin.bag.covidcertificate.verifier`](https://f-droid.org/packages/ch.admin.bag.covidcertificate.verifier)
* [`ch.admin.bag.covidcertificate.wallet`](https://f-droid.org/packages/ch.admin.bag.covidcertificate.wallet)
* [`com.markuspage.android.certtools`](https://f-droid.org/packages/com.markuspage.android.certtools) [missing]
* [`com.mishiranu.dashchan`](https://f-droid.org/packages/com.mishiranu.dashchan)
* [`de.corona.tracing`](https://f-droid.org/packages/de.corona.tracing)
* [`de.schildbach.oeffi`](https://f-droid.org/packages/de.schildbach.oeffi)
* [`eu.bubu1.fdroidclassic`](https://f-droid.org/packages/eu.bubu1.fdroidclassic)
* [`info.guardianproject.checkey`](https://f-droid.org/packages/info.guardianproject.checkey)
* [`nya.kitsunyan.foxydroid`](https://f-droid.org/packages/nya.kitsunyan.foxydroid)
* [`org.briarproject.briar.android`](https://f-droid.org/packages/org.briarproject.briar.android)
* [`org.jellyfin.androidtv`](https://f-droid.org/packages/org.jellyfin.androidtv) [disabled]
* [`org.jellyfin.mobile`](https://f-droid.org/packages/org.jellyfin.mobile)
* [`rs.ltt.android`](https://f-droid.org/packages/rs.ltt.android)
* [`top.fumiama.copymanga`](https://f-droid.org/packages/top.fumiama.copymanga)
* [`uk.co.keepawayfromfire.screens`](https://f-droid.org/packages/uk.co.keepawayfromfire.screens)

</details>

#### 2022-12-01: 25 apps (+ 11)

Newly added (none were removed):

<details>

* [`com.dhaval.bookland`](https://f-droid.org/packages/com.dhaval.bookland)
* [`com.github.bmx666.appcachecleaner`](https://f-droid.org/packages/com.github.bmx666.appcachecleaner) [signflinger]
* [`com.rafapps.earthviewformuzei`](https://f-droid.org/packages/com.rafapps.earthviewformuzei) [signflinger]
* [`com.zionhuang.music`](https://f-droid.org/packages/com.zionhuang.music)
* [`dev.yashgarg.qbit`](https://f-droid.org/packages/dev.yashgarg.qbit)
* [`io.github.project_kaat.gpsdrelay`](https://f-droid.org/packages/io.github.project_kaat.gpsdrelay)
* [`io.github.quillpad`](https://f-droid.org/packages/io.github.quillpad) [signflinger]
* [`me.gloeckl.fallasleep`](https://f-droid.org/packages/me.gloeckl.fallasleep)
* [`me.mudkip.moememos`](https://f-droid.org/packages/me.mudkip.moememos)
* [`org.joinmastodon.android`](https://f-droid.org/packages/org.joinmastodon.android) [signflinger]
* [`ru.ikkui.achie`](https://f-droid.org/packages/ru.ikkui.achie)

</details>

Signed with [`signflinger`](https://github.com/obfusk/apksigcopier#what-about-apks-signed-by-gradlezipflingersignflinger-instead-of-apksigner): 4 apps.

#### 2023-01-01: 41 apps (+ 16)

Newly added (none were removed):

<details>

* [`app.mlauncher`](https://f-droid.org/packages/app.mlauncher)
* [`com.akshayaap.mouseremote`](https://f-droid.org/packages/com.akshayaap.mouseremote) [signflinger]
* [`com.artikus.nolauncher`](https://f-droid.org/packages/com.artikus.nolauncher) [signflinger]
* [`com.dosse.clock31`](https://f-droid.org/packages/com.dosse.clock31) [signflinger]
* [`com.eurokonverter`](https://f-droid.org/packages/com.eurokonverter) [signflinger]
* [`com.github.cvzi.wallpaperexport`](https://f-droid.org/packages/com.github.cvzi.wallpaperexport) [signflinger]
* [`com.jroddev.android_oss_release_tracker`](https://f-droid.org/packages/com.jroddev.android_oss_release_tracker)
* [`com.martinmimigames.tinymusicplayer`](https://f-droid.org/packages/com.martinmimigames.tinymusicplayer) [signflinger]
* [`de.niendo.ImapNotes3`](https://f-droid.org/packages/de.niendo.ImapNotes3)
* [`dev.bartuzen.qbitcontroller`](https://f-droid.org/packages/dev.bartuzen.qbitcontroller) [signflinger]
* [`eu.auct.twitter2nitter`](https://f-droid.org/packages/eu.auct.twitter2nitter) [signflinger]
* [`nl.tsmeets.todotree`](https://f-droid.org/packages/nl.tsmeets.todotree)
* [`org.afrikalan.tuxmath`](https://f-droid.org/packages/org.afrikalan.tuxmath)
* [`org.asafonov.blockbuster`](https://f-droid.org/packages/org.asafonov.blockbuster)
* [`org.asafonov.monly`](https://f-droid.org/packages/org.asafonov.monly)
* [`org.greatfire.wikiunblocked.fdroid`](https://f-droid.org/packages/org.greatfire.wikiunblocked.fdroid) [signflinger]

</details>

Signed with [`signflinger`](https://github.com/obfusk/apksigcopier#what-about-apks-signed-by-gradlezipflingersignflinger-instead-of-apksigner): 14 apps.

#### 2023-02-01: 54 apps (+ 13)

Newly added (none were removed):

<details>

* [`InfinityLoop1309.NewPipeEnhanced`](https://f-droid.org/packages/InfinityLoop1309.NewPipeEnhanced) [signflinger]
* [`com.akansh.fileserversuit`](https://f-droid.org/packages/com.akansh.fileserversuit) [signflinger]
* [`com.nima.demomusix`](https://f-droid.org/packages/com.nima.demomusix) [signflinger]
* [`com.nima.taskmanager`](https://f-droid.org/packages/com.nima.taskmanager)
* [`com.nima.wikianime`](https://f-droid.org/packages/com.nima.wikianime) [signflinger]
* [`com.paranoiaworks.unicus.android.sse`](https://f-droid.org/packages/com.paranoiaworks.unicus.android.sse) [signflinger]
* [`com.razeeman.util.simpletimetracker`](https://f-droid.org/packages/com.razeeman.util.simpletimetracker) [signflinger]
* [`com.starry.myne`](https://f-droid.org/packages/com.starry.myne)
* [`de.andicodes.vergissnix`](https://f-droid.org/packages/de.andicodes.vergissnix)
* [`deltazero.amarok.foss`](https://f-droid.org/packages/deltazero.amarok.foss)
* [`io.github.yamin8000.dooz`](https://f-droid.org/packages/io.github.yamin8000.dooz) [signflinger]
* [`org.localsend.localsend_app`](https://f-droid.org/packages/org.localsend.localsend_app) [signflinger]
* [`yetzio.yetcalc`](https://f-droid.org/packages/yetzio.yetcalc) [signflinger]

</details>

Signed with [`signflinger`](https://github.com/obfusk/apksigcopier#what-about-apks-signed-by-gradlezipflingersignflinger-instead-of-apksigner): 23 apps.

#### 2023-03-01: 75 apps (+ 21)

Newly added (none were removed):

<details>

* [`com.akshayaap.touchdroid`](https://f-droid.org/packages/com.akshayaap.touchdroid) [signflinger]
* [`com.cyb3rko.pincredible`](https://f-droid.org/packages/com.cyb3rko.pincredible) [signflinger]
* [`com.github.vatbub.scoreboard`](https://f-droid.org/packages/com.github.vatbub.scoreboard) [signflinger]
* [`com.lijukay.quotesAltDesign`](https://f-droid.org/packages/com.lijukay.quotesAltDesign)
* [`com.nima.guessthatpokemon`](https://f-droid.org/packages/com.nima.guessthatpokemon) [signflinger]
* [`com.nima.mymood`](https://f-droid.org/packages/com.nima.mymood) [signflinger]
* [`com.zhenxiang.superimage`](https://f-droid.org/packages/com.zhenxiang.superimage)
* [`de.chadenas.cpudefense`](https://f-droid.org/packages/de.chadenas.cpudefense) [signflinger]
* [`de.westnordost.streetcomplete.expert`](https://f-droid.org/packages/de.westnordost.streetcomplete.expert) [signflinger]
* [`dev.datlag.burningseries`](https://f-droid.org/packages/dev.datlag.burningseries)
* [`eu.darken.capod`](https://f-droid.org/packages/eu.darken.capod)
* [`eu.zimbelstern.tournant`](https://f-droid.org/packages/eu.zimbelstern.tournant)
* [`gq.kirmanak.mealient`](https://f-droid.org/packages/gq.kirmanak.mealient)
* [`in.sunilpaulmathew.ashell`](https://f-droid.org/packages/in.sunilpaulmathew.ashell)
* [`org.dianqk.ruslin`](https://f-droid.org/packages/org.dianqk.ruslin)
* [`org.fcitx.fcitx5.android`](https://f-droid.org/packages/org.fcitx.fcitx5.android)
* [`ru.tech.imageresizershrinker`](https://f-droid.org/packages/ru.tech.imageresizershrinker)
* [`tk.hack5.treblecheck`](https://f-droid.org/packages/tk.hack5.treblecheck) [signflinger]
* [`ua.com.radiokot.lnaddr2invoice`](https://f-droid.org/packages/ua.com.radiokot.lnaddr2invoice) [signflinger]
* [`ua.syt0r.kanji.fdroid`](https://f-droid.org/packages/ua.syt0r.kanji.fdroid)
* [`website.leifs.delta.foss`](https://f-droid.org/packages/website.leifs.delta.foss)

</details>

Signed with [`signflinger`](https://github.com/obfusk/apksigcopier#what-about-apks-signed-by-gradlezipflingersignflinger-instead-of-apksigner): 32 apps.

#### 2023-04-01: 87 apps (+ 12)

Newly added (none were removed):

<details>

* [`com.bnyro.translate`](https://f-droid.org/packages/com.bnyro.translate) [signflinger]
* [`com.dessalines.thumbkey`](https://f-droid.org/packages/com.dessalines.thumbkey) [signflinger]
* [`com.julij.arsovreme`](https://f-droid.org/packages/com.julij.arsovreme) [signflinger]
* [`com.netvor.settings.database.provider`](https://f-droid.org/packages/com.netvor.settings.database.provider)
* [`com.vitorpamplona.amethyst`](https://f-droid.org/packages/com.vitorpamplona.amethyst)
* [`com.w2sv.wifiwidget`](https://f-droid.org/packages/com.w2sv.wifiwidget)
* [`de.ritscher.simplemobiletools.contacts.pro`](https://f-droid.org/packages/de.ritscher.simplemobiletools.contacts.pro) [signflinger]
* [`de.szalkowski.activitylauncher.rustore_fork`](https://f-droid.org/packages/de.szalkowski.activitylauncher.rustore_fork) [signflinger]
* [`io.github.zyrouge.symphony`](https://f-droid.org/packages/io.github.zyrouge.symphony)
* [`org.mindshub.insigno`](https://f-droid.org/packages/org.mindshub.insigno)
* [`player.phonograph.plus`](https://f-droid.org/packages/player.phonograph.plus)

</details>

No longer disabled:

<details>

* [`org.jellyfin.androidtv`](https://f-droid.org/packages/org.jellyfin.androidtv)

</details>

#### 2023-05-01: 104 apps (+ 17)

Newly added (none were removed):

<details>

* [`com.cyb3rko.pazzword`](https://f-droid.org/packages/com.cyb3rko.pazzword) [signflinger]
* [`com.hexbit.rutmath`](https://f-droid.org/packages/com.hexbit.rutmath) [signflinger]
* [`com.kaajjo.libresudoku`](https://f-droid.org/packages/com.kaajjo.libresudoku)
* [`com.thatsmanmeet.taskyapp`](https://f-droid.org/packages/com.thatsmanmeet.taskyapp)
* [`de.foodsharing.app`](https://f-droid.org/packages/de.foodsharing.app) [signflinger]
* [`development.parkenulm`](https://f-droid.org/packages/development.parkenulm)
* [`io.github.deweyreed.timer.other`](https://f-droid.org/packages/io.github.deweyreed.timer.other) [signflinger]
* [`io.github.muntashirakon.captiveportalcontroller`](https://f-droid.org/packages/io.github.muntashirakon.captiveportalcontroller) [signflinger]
* [`io.github.v2compose`](https://f-droid.org/packages/io.github.v2compose)
* [`net.viggers.zade.wallpaper`](https://f-droid.org/packages/net.viggers.zade.wallpaper)
* [`nl.privacydragon.bookwyrm`](https://f-droid.org/packages/nl.privacydragon.bookwyrm) [signflinger]
* [`org.cryptomator.lite`](https://f-droid.org/packages/org.cryptomator.lite)
* [`org.jshobbysoft.cameraalign`](https://f-droid.org/packages/org.jshobbysoft.cameraalign)
* [`ua.com.radiokot.photoprism`](https://f-droid.org/packages/ua.com.radiokot.photoprism) [signflinger]
* [`xyz.apiote.bimba.czwek`](https://f-droid.org/packages/xyz.apiote.bimba.czwek) [signflinger]

</details>

Switched to RB:

<details>

* [`com.wireguard.android`](https://f-droid.org/packages/com.wireguard.android)
* [`timur.webcall.callee`](https://f-droid.org/packages/timur.webcall.callee) [signflinger]

</details>

#### 2023-06-01: 116 apps (+ 14, - 2)

Newly added:

<details>

* [`com.amnesica.clearclipboard`](https://f-droid.org/packages/com.amnesica.clearclipboard)
* [`com.amnesica.kryptey`](https://f-droid.org/packages/com.amnesica.kryptey)
* [`com.atul.musicplayer`](https://f-droid.org/packages/com.atul.musicplayer) [signflinger]
* [`com.certified.audionote`](https://f-droid.org/packages/com.certified.audionote) [signflinger]
* [`com.gaika.bilketa`](https://f-droid.org/packages/com.gaika.bilketa) [signflinger]
* [`com.gokadzev.musify.fdroid`](https://f-droid.org/packages/com.gokadzev.musify.fdroid)
* [`com.prostudio.urltopdfconverter`](https://f-droid.org/packages/com.prostudio.urltopdfconverter) [signflinger]
* [`de.tu_chemnitz.etit.sse.openstop`](https://f-droid.org/packages/de.tu_chemnitz.etit.sse.openstop) [signflinger]
* [`dev.lbeernaert.youhavemail`](https://f-droid.org/packages/dev.lbeernaert.youhavemail)
* [`eu.mokrzycki.learndigits`](https://f-droid.org/packages/eu.mokrzycki.learndigits)
* [`github.umer0586.sensorserver`](https://f-droid.org/packages/github.umer0586.sensorserver) [signflinger]
* [`io.github.freewatermark.mobileapp`](https://f-droid.org/packages/io.github.freewatermark.mobileapp) [signflinger]
* [`io.github.friesi23.mhabit`](https://f-droid.org/packages/io.github.friesi23.mhabit) [signflinger]
* [`s1m.savertuner`](https://f-droid.org/packages/s1m.savertuner)

</details>

Switched away from RB:

<details>

* [`org.joinmastodon.android`](https://f-droid.org/packages/org.joinmastodon.android) [signflinger]

</details>

Archived:

<details>

* [`de.corona.tracing`](https://f-droid.org/packages/de.corona.tracing)

</details>

#### 2023-07-01: 137 apps (+ 21)

Newly added (none were removed):

<details>

* [`com.agateau.burgerparty`](https://f-droid.org/packages/com.agateau.burgerparty) [signflinger]
* [`com.codelv.inventory`](https://f-droid.org/packages/com.codelv.inventory)
* [`com.craftxbox.yubiclip.xor`](https://f-droid.org/packages/com.craftxbox.yubiclip.xor)
* [`com.dede.android_eggs`](https://f-droid.org/packages/com.dede.android_eggs) [signflinger]
* [`com.donnnno.arcticons.you`](https://f-droid.org/packages/com.donnnno.arcticons.you)
* [`com.flauschcode.broccoli`](https://f-droid.org/packages/com.flauschcode.broccoli)
* [`com.github.lamarios.clipious`](https://f-droid.org/packages/com.github.lamarios.clipious) [signflinger]
* [`com.github.muellerma.nfcreader`](https://f-droid.org/packages/com.github.muellerma.nfcreader)
* [`com.github.ttl.manager`](https://f-droid.org/packages/com.github.ttl.manager)
* [`com.kolserdav.ana`](https://f-droid.org/packages/com.kolserdav.ana) [signflinger]
* [`com.lighttigerxiv.simple.mp`](https://f-droid.org/packages/com.lighttigerxiv.simple.mp)
* [`com.maze_squirrel`](https://f-droid.org/packages/com.maze_squirrel) [signflinger]
* [`com.nyx.custom_uploader`](https://f-droid.org/packages/com.nyx.custom_uploader) [signflinger]
* [`com.sdcardstoryteller`](https://f-droid.org/packages/com.sdcardstoryteller)
* [`com.spencerpages`](https://f-droid.org/packages/com.spencerpages) [signflinger]
* [`com.wirelessalien.zipxtract`](https://f-droid.org/packages/com.wirelessalien.zipxtract) [signflinger]
* [`de.ptrlx.oneshot`](https://f-droid.org/packages/de.ptrlx.oneshot)
* [`dev.develsinthedetails.eatpoopyoucat`](https://f-droid.org/packages/dev.develsinthedetails.eatpoopyoucat) [signflinger]
* [`io.github.teccheck.fastlyrics`](https://f-droid.org/packages/io.github.teccheck.fastlyrics) [signflinger]
* [`org.fcitx.fcitx5.android.plugin.anthy`](https://f-droid.org/packages/org.fcitx.fcitx5.android.plugin.anthy)
* [`org.proninyaroslav.opencomicvine`](https://f-droid.org/packages/org.proninyaroslav.opencomicvine) [signflinger]

</details>

#### 2023-08-01: 157 apps (+ 20)

Newly added (none were removed):

<details>

* [`biz.binarysolutions.weatherusa`](https://f-droid.org/packages/biz.binarysolutions.weatherusa) [signflinger]
* [`bored.codebyk.mintcalc`](https://f-droid.org/packages/bored.codebyk.mintcalc) [signflinger]
* [`com.bnyro.clock`](https://f-droid.org/packages/com.bnyro.clock) [signflinger]
* [`com.bnyro.contacts`](https://f-droid.org/packages/com.bnyro.contacts) [signflinger]
* [`com.bnyro.recorder`](https://f-droid.org/packages/com.bnyro.recorder) [signflinger]
* [`com.bnyro.wallpaper`](https://f-droid.org/packages/com.bnyro.wallpaper) [signflinger]
* [`com.elasticrock.keepscreenon`](https://f-droid.org/packages/com.elasticrock.keepscreenon)
* [`com.etb.filemanager`](https://f-droid.org/packages/com.etb.filemanager)
* [`com.kounex.obsBlade`](https://f-droid.org/packages/com.kounex.obsBlade) [signflinger]
* [`com.nima.openbooksdownloader`](https://f-droid.org/packages/com.nima.openbooksdownloader) [signflinger]
* [`com.shifthackz.aisdv1.app.foss`](https://f-droid.org/packages/com.shifthackz.aisdv1.app.foss)
* [`com.willbsp.habits`](https://f-droid.org/packages/com.willbsp.habits)
* [`de.phrogg.bg2banglejs`](https://f-droid.org/packages/de.phrogg.bg2banglejs) [signflinger]
* [`eu.hydrologis.smash`](https://f-droid.org/packages/eu.hydrologis.smash) [signflinger]
* [`geddit.buzl.uk`](https://f-droid.org/packages/geddit.buzl.uk) [signflinger]
* [`io.github.doubi88.slideshowwallpaper`](https://f-droid.org/packages/io.github.doubi88.slideshowwallpaper)
* [`io.gitlab.pycpim.marxist`](https://f-droid.org/packages/io.gitlab.pycpim.marxist)
* [`nodo.crogers.exercisereminders`](https://f-droid.org/packages/nodo.crogers.exercisereminders)
* [`org.hzontal.tellaFOSS`](https://f-droid.org/packages/org.hzontal.tellaFOSS) [signflinger]
* [`vegabobo.dsusideloader`](https://f-droid.org/packages/vegabobo.dsusideloader)

</details>

#### 2023-09-01: 184 apps (+ 27)

Newly added (none were removed):

<details>

* [`app.michaelwuensch.bitbanana`](https://f-droid.org/packages/app.michaelwuensch.bitbanana)
* [`bored.codebyk.mint_task`](https://f-droid.org/packages/bored.codebyk.mint_task) [signflinger]
* [`cloud.pablos.overload`](https://f-droid.org/packages/cloud.pablos.overload)
* [`com.ammar.wallflow`](https://f-droid.org/packages/com.ammar.wallflow)
* [`com.baldo.bob`](https://f-droid.org/packages/com.baldo.bob)
* [`com.f0x1d.logfox`](https://f-droid.org/packages/com.f0x1d.logfox)
* [`com.geekorum.ttrss.free`](https://f-droid.org/packages/com.geekorum.ttrss.free)
* [`com.maxrave.simpmusic`](https://f-droid.org/packages/com.maxrave.simpmusic)
* [`com.noto`](https://f-droid.org/packages/com.noto) [signflinger]
* [`com.openstablediffusion`](https://f-droid.org/packages/com.openstablediffusion)
* [`com.upbad.apps.autonotify`](https://f-droid.org/packages/com.upbad.apps.autonotify)
* [`com.wirelessalien.android.bhagavadgita`](https://f-droid.org/packages/com.wirelessalien.android.bhagavadgita) [signflinger]
* [`dev.medzik.librepass.android`](https://f-droid.org/packages/dev.medzik.librepass.android)
* [`io.github.benderblog.traintime_pda`](https://f-droid.org/packages/io.github.benderblog.traintime_pda) [signflinger]
* [`io.github.pastthepixels.freepaint`](https://f-droid.org/packages/io.github.pastthepixels.freepaint)
* [`net.artificialworlds.boxstacker`](https://f-droid.org/packages/net.artificialworlds.boxstacker)
* [`net.e1547`](https://f-droid.org/packages/net.e1547) [signflinger]
* [`net.retiolus.cigalo`](https://f-droid.org/packages/net.retiolus.cigalo)
* [`net.stargw.applist`](https://f-droid.org/packages/net.stargw.applist)
* [`net.stargw.contacts`](https://f-droid.org/packages/net.stargw.contacts) [signflinger]
* [`net.stargw.fat`](https://f-droid.org/packages/net.stargw.fat) [signflinger]
* [`org.fcitx.fcitx5.android.plugin.clipboard_filter`](https://f-droid.org/packages/org.fcitx.fcitx5.android.plugin.clipboard_filter)
* [`org.privacymatters.safespace`](https://f-droid.org/packages/org.privacymatters.safespace)
* [`org.sirekanyan.knigopis`](https://f-droid.org/packages/org.sirekanyan.knigopis) [signflinger]
* [`org.sirekanyan.outline`](https://f-droid.org/packages/org.sirekanyan.outline)

</details>

Switched to RB:

<details>

* [`net.stargw.contactsimport`](https://f-droid.org/packages/net.stargw.contactsimport) [signflinger]
* [`net.stargw.fx`](https://f-droid.org/packages/net.stargw.fx)

</details>

#### 2023-10-01: 191 apps (+ 10, - 3)

Newly added:

<details>

* [`com.ammar.wallflow.plus`](https://f-droid.org/packages/com.ammar.wallflow.plus)
* [`com.chemistry.admin.chemistrylab`](https://f-droid.org/packages/com.chemistry.admin.chemistrylab) [signflinger]
* [`com.paultirk.yatoo`](https://f-droid.org/packages/com.paultirk.yatoo) [signflinger]
* [`de.wivewa.android`](https://f-droid.org/packages/de.wivewa.android)
* [`dev.anilbeesetti.nextplayer`](https://f-droid.org/packages/dev.anilbeesetti.nextplayer)
* [`dev.cyberme0w.openbike`](https://f-droid.org/packages/dev.cyberme0w.openbike)
* [`io.github.jd1378.otphelper`](https://f-droid.org/packages/io.github.jd1378.otphelper)
* [`io.github.mkckr0.audio_share_app`](https://f-droid.org/packages/io.github.mkckr0.audio_share_app)
* [`org.sirekanyan.warmongr`](https://f-droid.org/packages/org.sirekanyan.warmongr)
* [`se.arctosoft.vault`](https://f-droid.org/packages/se.arctosoft.vault)

</details>

Archived:

<details>

* [`ch.admin.bag.covidcertificate.verifier`](https://f-droid.org/packages/ch.admin.bag.covidcertificate.verifier)
* [`ch.admin.bag.covidcertificate.wallet`](https://f-droid.org/packages/ch.admin.bag.covidcertificate.wallet)

</details>

Disabled:

<details>

* [`org.sirekanyan.knigopis`](https://f-droid.org/packages/org.sirekanyan.knigopis)

</details>

---

Total number of apps using RB: 8 + 191 = 199.

---

### More graphs

![adds](../graphs/adds.png)

Description: graph "New apps (not 100% accurate)", showing new apps
added per month from 2022-11-01 to 2023-10-01, with an average of
about 25 new apps per month, with the fraction of those being
reproducible rising from about half to over two thirds.

![rems](../graphs/rems.png)

Description: graph "Removed apps (not 100% accurate)", showing apps
removed added per month from 2022-11-01 to 2023-10-01, with most
months seeing about 1-5 apps removed, and 5 months with 10-14 removed.

![apps](../graphs/apps.png)

Description: graph "F-Droid apps (not 100% accurate)", showing the
total number of apps per month from 2022-11-01 to 2023-10-01, about
4000, slowly increasing over time, and the fraction of those being
reproducible rising from almost none to about 5%.

![sigs](../graphs/sigs.png)

Description: graph "Apps published with Reproducible Builds
(signatures in metadata)", showing 6 apps on 2022-11-01, and 8 apps on
2023-10-01.

![bins](../graphs/bins.png)

Description: graph "Apps published with Reproducible Builds
(Binaries)", showing an almost straight line from 14 apps on
2022-11-01 to 191 apps on 2023-10-01.
