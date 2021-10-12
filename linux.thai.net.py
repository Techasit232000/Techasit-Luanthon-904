Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("
<!DOCTYPE html>
<html  lang="en" dir="ltr">
<head>
  <meta charset="utf-8" />
<meta name="Generator" content="Drupal 7 (http://drupal.org)" />
<link rel="alternate" type="application/rss+xml" title="LTN -- linux.thai.net  RSS" href="https://linux.thai.net/rss.xml" />
<link rel="shortcut icon" href="https://linux.thai.net/files/favicon.ico" type="image/vnd.microsoft.icon" />
  <title>LTN -- linux.thai.net  | คนไทยใช้ลินุกซ์</title>

      <meta name="MobileOptimized" content="width">
    <meta name="HandheldFriendly" content="true">
    <meta name="viewport" content="width=device-width">
  
  <link type="text/css" rel="stylesheet" href="https://linux.thai.net/files/css/css_HMdgmP_ruq04JMG4Y1ltGeUYDBUUuqnqj-3dcqRaaj0.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://linux.thai.net/files/css/css_Gn8vFuzUmpB5Lsvcx7Mvj78tnGSi8QgRfRK8qfVyxnY.css" media="all" />
  <script src="https://linux.thai.net/misc/jquery.js?v=1.4.4"></script>
<script src="https://linux.thai.net/misc/jquery.once.js?v=1.2"></script>
<script src="https://linux.thai.net/misc/drupal.js?qhgb7y"></script>
<script>jQuery.extend(Drupal.settings, {"basePath":"\/","pathPrefix":"","ajaxPageState":{"theme":"ltn","theme_token":"j4K6H09wC2lw6XAZGNGXl49mNej7F7PPdqf0Mq-FdoY","js":{"misc\/jquery.js":1,"misc\/jquery.once.js":1,"misc\/drupal.js":1},"css":{"modules\/system\/system.base.css":1,"modules\/system\/system.menus.css":1,"modules\/system\/system.messages.css":1,"modules\/system\/system.theme.css":1,"modules\/aggregator\/aggregator.css":1,"modules\/book\/book.css":1,"modules\/field\/theme\/field.css":1,"modules\/node\/node.css":1,"modules\/search\/search.css":1,"modules\/user\/user.css":1,"themes\/local\/ltn\/system.base.css":1,"themes\/local\/ltn\/system.menus.css":1,"themes\/local\/ltn\/system.messages.css":1,"themes\/local\/ltn\/system.theme.css":1,"themes\/local\/ltn\/comment.css":1,"themes\/local\/ltn\/node.css":1,"themes\/local\/ltn\/css\/styles.css":1}},"urlIsAjaxTrusted":{"\/node?destination=node":true}});</script>
  </head>
<body class="html front not-logged-in two-sidebars page-node" >
      <p class="skip-link__wrapper">
      <a href="#main-menu" class="skip-link visually-hidden visually-hidden--focusable" id="skip-link">Jump to navigation</a>
    </p>
      
<div class="layout-center">

  <header class="header" role="banner">

          <a href="/" title="Home" rel="home" class="header__logo"><img src="https://linux.thai.net/files/logo.png" alt="Home" class="header__logo-image" /></a>
    
    
    
    
  </header>

  <div class="layout-3col layout-swap">

    
    <main class="layout-3col__right-content" role="main">
                  <a href="#skip-link" class="visually-hidden visually-hidden--focusable" id="main-content">Back to top</a>
                                                


<article class="node node-story node-promoted node-teaser clearfix node-317">

      <header>
                    <h2><a href="/node/317">libdatrie 0.2.13 Released</a></h2>
            
              <p class="submitted">
                    Submitted by <span class="username">thep</span> on <time pubdate datetime="2021-01-29T17:34:00+07:00">29 January, 2021 - 17:34</time>        </p>
      
          </header>
  
  <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><h3>Changes from 0.2.12</h3>
<ul><li> Fix wrong key listing in byte trie<br />
       (<a href="https://github.com/tlwg/libdatrie/issues/9">Issue #9</a>, Thanks @legale for the report.) </li>
<li> Fix cross-compiling issue caused by AC_FUNC_MALLOC<br />
       (<a href="https://github.com/tlwg/libdatrie/issues/11">Issue #11</a>, Thanks Vanessa McHale for the report.) </li>
<li> Fix isspace() arg problem on NetBSD.<br />
       (Personal mail, Thanks Sean for the report;<br /><a href="https://github.com/tlwg/libdatrie/pull/8">PR #8</a>, Thanks OBATA Akio for an independent pull request.) </li>
<li> Fix some documentations. </li>
<li> Really use TRIE_CHAR_TERM in TrieChar string termination.<br />
       Changing TRIE_CHAR_TERM definition now won't break the code. </li>
<li> Fix Windows build issue by avoiding &lt;unistd.h&gt; include.<br />
       (Partially addressing <a href="https://github.com/tlwg/libdatrie/pull/15">PR #15</a>, Thanks @fanc999 for first raising this.) </li>
<li> [New APIs] Add serialization of the trie into memory buffer.<br />
       (<a href="https://github.com/tlwg/libdatrie/pull/12">PR #12</a>, Thanks KOLANICH for the contribution.) </li>
</ul></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-above"><div class="field-label">Projects:&nbsp;</div><div class="field-items"><div class="field-item even"><a href="/taxonomy/term/1">libthai</a></div></div></div>
  <ul class="links inline"><li class="node-readmore first last"><a href="/node/317" rel="tag" title="libdatrie 0.2.13 Released">Read more<span class="element-invisible"> about libdatrie 0.2.13 Released</span></a></li>
</ul>
  
</article>
<article class="node node-story node-promoted node-teaser clearfix node-316">

      <header>
                    <h2><a href="/node/316">Fonts-TLWG 0.7.2 Released</a></h2>
            
              <p class="submitted">
                    Submitted by <span class="username">thep</span> on <time pubdate datetime="2020-05-01T11:38:13+07:00">1 May, 2020 - 11:38</time>        </p>
      
          </header>
  
  <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><h3>Changes from 0.7.1</h3>
<ul><li> Garuda has been fine-tuned by hand for balanced cubic splines and optimal quadratic splines. </li>
<li> All families now use OS/2 Typo metrics instead of just Win/Hhea metrics.
</li>
<li> The OS/2 Typo metrics of each family have been normalized for equal line spacing on all faces, esp. regular and bold. </li>
<li> Switch to Python 3 on build scripts. </li>
<li> Fix a TDS zipball naming issue in the generated CTAN zipball. </li>
</ul><h3>Download</h3></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-above"><div class="field-label">Projects:&nbsp;</div><div class="field-items"><div class="field-item even"><a href="/taxonomy/term/3">Fonts-TLWG</a></div></div></div>
  <ul class="links inline"><li class="node-readmore first last"><a href="/node/316" rel="tag" title="Fonts-TLWG 0.7.2 Released">Read more<span class="element-invisible"> about Fonts-TLWG 0.7.2 Released</span></a></li>
</ul>
  
</article>
<article class="node node-story node-promoted node-teaser clearfix node-315">

      <header>
                    <h2><a href="/node/315">Fonts-Arundina 0.3.2 Released</a></h2>
            
              <p class="submitted">
                    Submitted by <span class="username">thep</span> on <time pubdate datetime="2020-02-12T16:21:41+07:00">12 February, 2020 - 16:21</time>        </p>
      
          </header>
  
  <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><h3>Changes from Fonts-SIPA-Arundina 0.3.1</h3>
<ul><li> Set OS/2 metrics for proper line spacing. </li>
<li> Fix broken TDS compliance in CTAN zipball. </li>
<li> Update links in README. </li>
</ul><h3>Download</h3>
<ul><li> source: <a href="ftp://linux.thai.net/pub/thailinux/software/fonts-arundina/fonts-arundina-0.3.2.tar.xz">ftp://linux.thai.net/pub/thailinux/software/fonts-arundina/fonts-arundin...</a> </li></ul></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-above"><div class="field-label">Projects:&nbsp;</div><div class="field-items"><div class="field-item even"><a href="/taxonomy/term/26">Fonts-SIPA-Arundina</a></div></div></div>
  <ul class="links inline"><li class="node-readmore first last"><a href="/node/315" rel="tag" title="Fonts-Arundina 0.3.2 Released">Read more<span class="element-invisible"> about Fonts-Arundina 0.3.2 Released</span></a></li>
</ul>
  
</article>
<article class="node node-story node-promoted node-teaser clearfix node-314">

      <header>
                    <h2><a href="/node/314">Fonts-Arundina 0.3.1 Released</a></h2>
            
              <p class="submitted">
                    Submitted by <span class="username">thep</span> on <time pubdate datetime="2020-01-29T15:13:29+07:00">29 January, 2020 - 15:13</time>        </p>
      
          </header>
  
  <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><h3>Changes from Fonts-SIPA-Arundina 0.3.0</h3>
<ul><li> Fix CTAN zipball build failure. </li>
<li> Allow installable font embedding (issue caught by Debian's lintian). </li>
</ul><h3>Download</h3>
<ul><li> source: <a href="ftp://linux.thai.net/pub/thailinux/software/fonts-arundina/fonts-arundina-0.3.1.tar.xz">ftp://linux.thai.net/pub/thailinux/software/fonts-arundina/fonts-arundin...</a> </li>
<li> binary (TTF): <a href="ftp://linux.thai.net/pub/thailinux/software/fonts-arundina/ttf-arundina-0.3.1.tar.xz">ftp://linux.thai.net/pub/thailinux/software/fonts-arundina/ttf-arundina-...</a> </li></ul></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-above"><div class="field-label">Projects:&nbsp;</div><div class="field-items"><div class="field-item even"><a href="/taxonomy/term/26">Fonts-SIPA-Arundina</a></div></div></div>
  <ul class="links inline"><li class="node-readmore first last"><a href="/node/314" rel="tag" title="Fonts-Arundina 0.3.1 Released">Read more<span class="element-invisible"> about Fonts-Arundina 0.3.1 Released</span></a></li>
</ul>
  
</article>
<article class="node node-story node-promoted node-teaser clearfix node-313">

      <header>
                    <h2><a href="/node/313">Fonts-Arundina 0.3.0 Released</a></h2>
            
              <p class="submitted">
                    Submitted by <span class="username">thep</span> on <time pubdate datetime="2020-01-22T15:34:51+07:00">22 January, 2020 - 15:34</time>        </p>
      
          </header>
  
  <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><p>"Fonts-SIPA-Arundina" project is now renamed to "Fonts-Arundina".</p></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-above"><div class="field-label">Projects:&nbsp;</div><div class="field-items"><div class="field-item even"><a href="/taxonomy/term/26">Fonts-SIPA-Arundina</a></div></div></div>
  <ul class="links inline"><li class="node-readmore first last"><a href="/node/313" rel="tag" title="Fonts-Arundina 0.3.0 Released">Read more<span class="element-invisible"> about Fonts-Arundina 0.3.0 Released</span></a></li>
</ul>
  
</article>
<article class="node node-story node-promoted node-teaser clearfix node-312">

      <header>
                    <h2><a href="/node/312">gtk-im-libthai-0.2.2 Released</a></h2>
            
              <p class="submitted">
                    Submitted by <span class="username">thep</span> on <time pubdate datetime="2019-08-03T13:59:39+07:00">3 August, 2019 - 13:59</time>        </p>
      
          </header>
  
  <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><h3>Changes from 0.2.1</h3>
<ul><li> Drop usage of deprecated GTK+ API </li>
<li> Working 'make distcheck' </li>
<li> XZ release tarball compression </li>
<li> New configure option to disable fallback (Use with care!) </li>
</ul><h3>Download</h3>
<p><a href="ftp://linux.thai.net/pub/ThaiLinux/software/libthai/gtk-im-libthai-0.2.2.tar.xz">ftp://linux.thai.net/pub/ThaiLinux/software/libthai/gtk-im-libthai-0.2.2...</a></p></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-above"><div class="field-label">Projects:&nbsp;</div><div class="field-items"><div class="field-item even"><a href="/taxonomy/term/1">libthai</a></div></div></div>
  <ul class="links inline"><li class="node-readmore first last"><a href="/node/312" rel="tag" title="gtk-im-libthai-0.2.2 Released">Read more<span class="element-invisible"> about gtk-im-libthai-0.2.2 Released</span></a></li>
</ul>
  
</article>
<article class="node node-story node-promoted node-teaser clearfix node-311">

      <header>
                    <h2><a href="/node/311">Fonts-TLWG 0.7.1 Released</a></h2>
            
              <p class="submitted">
                    Submitted by <span class="username">thep</span> on <time pubdate datetime="2018-11-04T16:18:31+07:00">4 November, 2018 - 16:18</time>        </p>
      
          </header>
  
  <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><h3>Changes from 0.7.0</h3>
<ul><li> Address another reproducibility issue caused by "date stamp" in auto-generated UniqueID.
       </li>
<li> Automate font binary tarballs building, with additional ZIP provision. </li>
</ul><h3>Download</h3>
<ul><li> source: <a href="ftp://linux.thai.net/pub/thailinux/software/fonts-tlwg/fonts-tlwg-0.7.1.tar.xz">ftp://linux.thai.net/pub/thailinux/software/fonts-tlwg/fonts-tlwg-0.7.1....</a> </li>
<li> binary (OTF):</li></ul></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-above"><div class="field-label">Projects:&nbsp;</div><div class="field-items"><div class="field-item even"><a href="/taxonomy/term/3">Fonts-TLWG</a></div></div></div>
  <ul class="links inline"><li class="node-readmore first last"><a href="/node/311" rel="tag" title="Fonts-TLWG 0.7.1 Released">Read more<span class="element-invisible"> about Fonts-TLWG 0.7.1 Released</span></a></li>
</ul>
  
</article>
<article class="node node-story node-promoted node-teaser clearfix node-310">

      <header>
                    <h2><a href="/node/310">Fonts-TLWG 0.7.0 Released</a></h2>
            
              <p class="submitted">
                    Submitted by <span class="username">thep</span> on <time pubdate datetime="2018-10-26T14:32:53+07:00">26 October, 2018 - 14:32</time>        </p>
      
          </header>
  
  <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><h3>Changes from 0.6.5</h3>
<ul><li> Build fonts reproducibly, thus new major version due to source restructuring.
       </li>
<li> Generate OTF by default instead of TTF. </li>
<li> LaTeX: Provide OpenType fonts for XeTeX.<br />
       (<a href="https://github.com/tlwg/fonts-tlwg/issues/6">Issue #6</a>. Thanks <a href="https://github.com/abhabongse">Abhabongse Janthong</a> for the suggestion.)
       </li>
<li> Fix bug in GSUB rule.<br />
       (<a href="https://github.com/tlwg/fonts-tlwg/issues/7">Issue #7</a>. Thanks <a href="https://github.com/Richard57">@Richard57</a> for the report and investigation.)
       </li>
<li> Norasi: Fix Fontforge warnings and substitution rules. </li>
</ul></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-above"><div class="field-label">Projects:&nbsp;</div><div class="field-items"><div class="field-item even"><a href="/taxonomy/term/3">Fonts-TLWG</a></div></div></div>
  <ul class="links inline"><li class="node-readmore first last"><a href="/node/310" rel="tag" title="Fonts-TLWG 0.7.0 Released">Read more<span class="element-invisible"> about Fonts-TLWG 0.7.0 Released</span></a></li>
</ul>
  
</article>
<article class="node node-story node-promoted node-teaser clearfix node-309">

      <header>
                    <h2><a href="/node/309">Announcing thpronun 0.2.0</a></h2>
            
              <p class="submitted">
                    Submitted by <span class="username">thep</span> on <time pubdate datetime="2018-08-29T12:41:42+07:00">29 August, 2018 - 12:41</time>        </p>
      
          </header>
  
  <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><p>thpronun is a program for analyzing pronunciation of Thai words. The output can be in Thai pronunciation, Romanization, or in any other phonetic systems. It is designed to be extensible.</p>
<p>This software is provided as free software under the sponsorship of <a href="https://mm.co.th/">Metamedia Technology Co., Ltd.</a></p></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-above"><div class="field-label">Projects:&nbsp;</div><div class="field-items"><div class="field-item even"><a href="/taxonomy/term/30">thpronun</a></div></div></div>
  <ul class="links inline"><li class="node-readmore first last"><a href="/node/309" rel="tag" title="Announcing thpronun 0.2.0">Read more<span class="element-invisible"> about Announcing thpronun 0.2.0</span></a></li>
</ul>
  
</article>
<article class="node node-story node-promoted node-teaser clearfix node-308">

      <header>
                    <h2><a href="/node/308">swath 0.6.1 Released</a></h2>
            
              <p class="submitted">
                    Submitted by <span class="username">thep</span> on <time pubdate datetime="2018-08-20T12:08:00+07:00">20 August, 2018 - 12:08</time>        </p>
      
          </header>
  
  <div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><h3>Changes from 0.6.0</h3>
<ul><li> Updated word break dictionary. </li>
<li> Fix a defect in RTF parsing, so RTF gets more complete word break positions. </li>
<li> Compiler warning fixes. </li>
<li> Minor code cleanups. </li>
<li> Useful installation instructions in INSTALL file.<br />
        (Thanks <a href="https://github.com/pepa65">@pepa65</a> for the pull request.) </li>
</ul><h3>Download</h3>
<p><a href="ftp://linux.thai.net/pub/thailinux/software/swath/swath-0.6.1.tar.xz">ftp://linux.thai.net/pub/thailinux/software/swath/swath-0.6.1.tar.xz</a></p></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-above"><div class="field-label">Projects:&nbsp;</div><div class="field-items"><div class="field-item even"><a href="/taxonomy/term/4">ThaiLaTeX</a></div></div></div>
  <ul class="links inline"><li class="node-readmore first last"><a href="/node/308" rel="tag" title="swath 0.6.1 Released">Read more<span class="element-invisible"> about swath 0.6.1 Released</span></a></li>
</ul>
  
</article>
<h2 class="element-invisible">Pages</h2><div class="item-list"><ul class="pager"><li class="pager-current first">1</li>
<li class="pager-item"><a title="Go to page 2" href="/node?page=1">2</a></li>
<li class="pager-item"><a title="Go to page 3" href="/node?page=2">3</a></li>
<li class="pager-item"><a title="Go to page 4" href="/node?page=3">4</a></li>
<li class="pager-item"><a title="Go to page 5" href="/node?page=4">5</a></li>
<li class="pager-item"><a title="Go to page 6" href="/node?page=5">6</a></li>
<li class="pager-item"><a title="Go to page 7" href="/node?page=6">7</a></li>
<li class="pager-item"><a title="Go to page 8" href="/node?page=7">8</a></li>
<li class="pager-item"><a title="Go to page 9" href="/node?page=8">9</a></li>
<li class="pager-ellipsis">…</li>
<li class="pager-next"><a title="Go to next page" href="/node?page=1">next ›</a></li>
<li class="pager-last last"><a title="Go to last page" href="/node?page=13">last »</a></li>
</ul></div>      <a href="/rss.xml" class="feed-icon" title="Subscribe to LTN -- linux.thai.net  RSS"><img src="https://linux.thai.net/misc/feed.png" width="16" height="16" alt="Subscribe to LTN -- linux.thai.net  RSS" /></a>    </main>

    <div class="layout-swap__top layout-3col__full">

      <a href="#skip-link" class="visually-hidden visually-hidden--focusable" id="main-menu" tabindex="-1">Back to top</a>

      
      
    </div>

          <aside class="layout-3col__first-left-sidebar" role="complementary">
        
<div class="block block-block first odd" id="block-block-4">

        <h2 class="block__title">Community</h2>
    
  <ul><li> <a href="http://linux.thai.net/planet">Planet</a> </li>
<li> IRC
<ul><li> <a href="irc://irc.oftc.net/#tlwg">#tlwg at OFTC</a> </li>
<li> <a href="https://webchat.oftc.net/?channels=tlwg ">Web Chat</a> </li>
<li> <a href="https://riot.im/app/#/room/%23_oftc_%23tlwg:matrix.org">by Riot</a> </li>
</ul></li></ul>
</div>
<div class="block block-menu even" role="navigation" id="block-menu-menu-resource">

        <h2 class="block__title">Resource</h2>
    
  <ul class="menu"><li class="menu__item is-expanded first expanded"><a href="/projects" title="Projects" class="menu__link">Projects</a><ul class="menu"><li class="menu__item is-leaf first leaf"><a href="/projects/libthai" title="libthai Library" class="menu__link">libthai</a></li>
<li class="menu__item is-leaf leaf"><a href="/projects/firefox-thai" title="Information about Mozilla Firefox browser with Thai language support" class="menu__link">Firefox Thai</a></li>
<li class="menu__item is-leaf leaf"><a href="/projects/thaixfonts" title="A collection of Thai bitmap fonts available in free licenses" class="menu__link">Thai X Fonts</a></li>
<li class="menu__item is-leaf leaf"><a href="/projects/fonts-tlwg" title="A collection of Thai scalable fonts available in free licenses" class="menu__link">Fonts-TLWG</a></li>
<li class="menu__item is-leaf leaf"><a href="/projects/fonts-sipa-arundina" title="Bitstream Vera/Dejavu compatible fonts" class="menu__link">Fonts-SIPA-Arundina</a></li>
<li class="menu__item is-leaf leaf"><a href="/projects/thaifonts-siampradesh" title="Fonts based on DIP/SIPA contested fonts" class="menu__link">Fonts-SiamPradesh</a></li>
<li class="menu__item is-leaf leaf"><a href="/projects/thailatex" title="A Thai package which enables typesetting Thai with LaTeX&#039;s standard document classes" class="menu__link">ThaiLaTeX</a></li>
<li class="menu__item is-leaf leaf"><a href="/projects/swath" title="SWATH" class="menu__link">SWATH</a></li>
<li class="menu__item is-leaf last leaf"><a href="/projects/thai-kde-qt" title="Thai language support for KDE/Qt development" class="menu__link">Thai in KDE/Qt</a></li>
</ul></li>
<li class="menu__item is-expanded expanded"><a href="/download" title="Download useful stuff" class="menu__link">Download</a><ul class="menu"><li class="menu__item is-leaf first leaf"><a href="/github" title="TLWG Software Repository at GitHub" class="menu__link">GitHub</a></li>
<li class="menu__item is-leaf last leaf"><a href="ftp://linux.thai.net/pub" title="Thai Linux related files" class="menu__link">Thai Linux FTP</a></li>
</ul></li>
<li class="menu__item is-leaf last leaf"><a href="http://th.lug.wikia.com/wiki/Tlwg_todo_list" title="TLWG Developers&#039; Todo List" class="menu__link">Developers&#039; Todo</a></li>
</ul>
</div>
<div class="block block-user odd" role="form" id="block-user-login">

        <h2 class="block__title">User login</h2>
    
  <form action="/node?destination=node" method="post" id="user-login-form" accept-charset="UTF-8"><div><div class="form-item form-type-textfield form-item-name">
  <label for="edit-name">Username <span class="form-required" title="This field is required.">*</span></label>
 <input type="text" id="edit-name" name="name" value="" size="15" maxlength="60" class="form-text required" />
</div>
<div class="form-item form-type-password form-item-pass">
  <label for="edit-pass">Password <span class="form-required" title="This field is required.">*</span></label>
 <input type="password" id="edit-pass" name="pass" size="15" maxlength="128" class="form-text required" />
</div>
<div class="item-list"><ul><li class="first last"><a href="/user/password" title="Request new password via e-mail.">Request new password</a></li>
</ul></div><input type="hidden" name="form_build_id" value="form-XCuR__GO29-c7zy0GqwaH9HTjll35NaeLpE-2pZNcHY" />
<input type="hidden" name="form_id" value="user_login_block" />
<div class="form-actions form-wrapper" id="edit-actions"><input type="submit" id="edit-submit" name="op" value="Log in" class="form-submit" /></div></div></form>
</div>
<div class="block block-block last even" id="block-block-1">

        <h2 class="block__title">External Links</h2>
    
  <ul class="menu"><li class="expanded">About<br /><ul class="menu"><li class="leaf"><a href="/about/history">History</a></li>
</ul></li>
</ul><ul class="menu"><li class="expanded">Linux and FOSS<br /><ul class="menu"><li class="leaf"><a href="http://debianclub.org">Debian Club</a></li>
<li class="leaf"><a href="http://www.ubuntuclub.com">Ubuntu Club</a></li>
</ul></li><li class="expanded">Others<br /><ul class="menu"><li class="leaf"><a href="http://blognone.com">Blognone</a></li>
</ul></li></ul>
</div>
      </aside>
    
          <aside class="layout-3col__second-left-sidebar" role="complementary">
        
<div class="block block-aggregator first last odd" role="complementary" id="block-aggregator-feed-4">

        <h2 class="block__title">Planet TLWG</h2>
    
  <div class="item-list"><ul><li class="first"><a href="http://vee-r.blogspot.com/2021/08/i-moved-to-devtoveer66.html">Vee: I moved to dev.to/veer66.</a>
</li>
<li><a href="https://kitty.in.th/index.php/2020/02/12/kobe-b-bryant/">Kitt: Kobe B. Bryant</a>
</li>
<li class="last"><a href="http://thep.blogspot.com/2021/06/norasi-small-caps-and-old-style-figures.html">Thep: Norasi Small Caps and Old Style Figures</a>
</li>
</ul></div><div class="more-link"><a href="/aggregator/sources/4" title="View this feed&#039;s recent news.">More</a></div>
</div>
      </aside>
    
  </div>

  
</div>

  </body>
</html>
")
	
SyntaxError: EOL while scanning string literal
>>> print ("Username Techasit14607")
Username Techasit14607
>>> print ("Password @Techasit1198837")
Password @Techasit1198837
>>> print ("linux.thai.net")
linux.thai.net
>>> 