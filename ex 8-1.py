<!DOCTYPE html>
<!-- saved from url=(0061)https://www.programiz.com/python-programming/online-compiler/ -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style>    .error_widget_wrapper {        background: inherit;        color: inherit;        border:none    }    .error_widget {        border-top: solid 2px;        border-bottom: solid 2px;        margin: 5px 0;        padding: 10px 40px;        white-space: pre-wrap;    }    .error_widget.ace_error, .error_widget_arrow.ace_error{        border-color: #ff5a5a    }    .error_widget.ace_warning, .error_widget_arrow.ace_warning{        border-color: #F1D817    }    .error_widget.ace_info, .error_widget_arrow.ace_info{        border-color: #5a5a5a    }    .error_widget.ace_ok, .error_widget_arrow.ace_ok{        border-color: #5aaa5a    }    .error_widget_arrow {        position: absolute;        border: solid 5px;        border-top-color: transparent!important;        border-right-color: transparent!important;        border-left-color: transparent!important;        top: -5px;    }</style><style id="ace-tm">.ace-tm .ace_gutter {background: #f0f0f0;color: #333;}.ace-tm .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-tm .ace_fold {background-color: #6B72E6;}.ace-tm {background-color: #FFFFFF;color: black;}.ace-tm .ace_cursor {color: black;}.ace-tm .ace_invisible {color: rgb(191, 191, 191);}.ace-tm .ace_storage,.ace-tm .ace_keyword {color: blue;}.ace-tm .ace_constant {color: rgb(197, 6, 11);}.ace-tm .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-tm .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-tm .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-tm .ace_invalid {background-color: rgba(255, 0, 0, 0.1);color: red;}.ace-tm .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-tm .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-tm .ace_support.ace_type,.ace-tm .ace_support.ace_class {color: rgb(109, 121, 222);}.ace-tm .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-tm .ace_string {color: rgb(3, 106, 7);}.ace-tm .ace_comment {color: rgb(76, 136, 107);}.ace-tm .ace_comment.ace_doc {color: rgb(0, 102, 255);}.ace-tm .ace_comment.ace_doc.ace_tag {color: rgb(128, 159, 191);}.ace-tm .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-tm .ace_variable {color: rgb(49, 132, 149);}.ace-tm .ace_xml-pe {color: rgb(104, 104, 91);}.ace-tm .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-tm .ace_heading {color: rgb(12, 7, 255);}.ace-tm .ace_list {color:rgb(185, 6, 144);}.ace-tm .ace_meta.ace_tag {color:rgb(0, 22, 142);}.ace-tm .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-tm .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-tm.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-tm .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-tm .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-tm .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-tm .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-tm .ace_gutter-active-line {background-color : #dcdcdc;}.ace-tm .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-tm .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-tm */</style><style id="ace_editor.css">.ace_br1 {border-top-left-radius    : 3px;}.ace_br2 {border-top-right-radius   : 3px;}.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}.ace_br4 {border-bottom-right-radius: 3px;}.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}.ace_br8 {border-bottom-left-radius : 3px;}.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}.ace_editor {position: relative;overflow: hidden;padding: 0;font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;direction: ltr;text-align: left;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);}.ace_scroller {position: absolute;overflow: hidden;top: 0;bottom: 0;background-color: inherit;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;cursor: text;}.ace_content {position: absolute;box-sizing: border-box;min-width: 100%;contain: style size layout;font-variant-ligatures: no-common-ligatures;}.ace_dragging .ace_scroller:before{position: absolute;top: 0;left: 0;right: 0;bottom: 0;content: '';background: rgba(250, 250, 250, 0.01);z-index: 1000;}.ace_dragging.ace_dark .ace_scroller:before{background: rgba(0, 0, 0, 0.01);}.ace_selecting, .ace_selecting * {cursor: text !important;}.ace_gutter {position: absolute;overflow : hidden;width: auto;top: 0;bottom: 0;left: 0;cursor: default;z-index: 4;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;contain: style size layout;}.ace_gutter-active-line {position: absolute;left: 0;right: 0;}.ace_scroller.ace_scroll-left {box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;}.ace_gutter-cell {position: absolute;top: 0;left: 0;right: 0;padding-left: 19px;padding-right: 6px;background-repeat: no-repeat;}.ace_gutter-cell.ace_error {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: 2px center;}.ace_gutter-cell.ace_warning {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");background-position: 2px center;}.ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");background-position: 2px center;}.ace_dark .ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");}.ace_scrollbar {contain: strict;position: absolute;right: 0;bottom: 0;z-index: 6;}.ace_scrollbar-inner {position: absolute;cursor: text;left: 0;top: 0;}.ace_scrollbar-v{overflow-x: hidden;overflow-y: scroll;top: 0;}.ace_scrollbar-h {overflow-x: scroll;overflow-y: hidden;left: 0;}.ace_print-margin {position: absolute;height: 100%;}.ace_text-input {position: absolute;z-index: 0;width: 0.5em;height: 1em;opacity: 0;background: transparent;-moz-appearance: none;appearance: none;border: none;resize: none;outline: none;overflow: hidden;font: inherit;padding: 0 1px;margin: 0 -1px;contain: strict;-ms-user-select: text;-moz-user-select: text;-webkit-user-select: text;user-select: text;white-space: pre!important;}.ace_text-input.ace_composition {background: transparent;color: inherit;z-index: 1000;opacity: 1;}.ace_composition_placeholder { color: transparent }.ace_composition_marker { border-bottom: 1px solid;position: absolute;border-radius: 0;margin-top: 1px;}[ace_nocontext=true] {transform: none!important;filter: none!important;clip-path: none!important;mask : none!important;contain: none!important;perspective: none!important;mix-blend-mode: initial!important;z-index: auto;}.ace_layer {z-index: 1;position: absolute;overflow: hidden;word-wrap: normal;white-space: pre;height: 100%;width: 100%;box-sizing: border-box;pointer-events: none;}.ace_gutter-layer {position: relative;width: auto;text-align: right;pointer-events: auto;height: 1000000px;contain: style size layout;}.ace_text-layer {font: inherit !important;position: absolute;height: 1000000px;width: 1000000px;contain: style size layout;}.ace_text-layer > .ace_line, .ace_text-layer > .ace_line_group {contain: style size layout;position: absolute;top: 0;left: 0;right: 0;}.ace_hidpi .ace_text-layer,.ace_hidpi .ace_gutter-layer,.ace_hidpi .ace_content,.ace_hidpi .ace_gutter {contain: strict;will-change: transform;}.ace_hidpi .ace_text-layer > .ace_line, .ace_hidpi .ace_text-layer > .ace_line_group {contain: strict;}.ace_cjk {display: inline-block;text-align: center;}.ace_cursor-layer {z-index: 4;}.ace_cursor {z-index: 4;position: absolute;box-sizing: border-box;border-left: 2px solid;transform: translatez(0);}.ace_multiselect .ace_cursor {border-left-width: 1px;}.ace_slim-cursors .ace_cursor {border-left-width: 1px;}.ace_overwrite-cursors .ace_cursor {border-left-width: 0;border-bottom: 1px solid;}.ace_hidden-cursors .ace_cursor {opacity: 0.2;}.ace_hasPlaceholder .ace_hidden-cursors .ace_cursor {opacity: 0;}.ace_smooth-blinking .ace_cursor {transition: opacity 0.18s;}.ace_animate-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: step-end;animation-name: blink-ace-animate;animation-iteration-count: infinite;}.ace_animate-blinking.ace_smooth-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: ease-in-out;animation-name: blink-ace-animate-smooth;}@keyframes blink-ace-animate {from, to { opacity: 1; }60% { opacity: 0; }}@keyframes blink-ace-animate-smooth {from, to { opacity: 1; }45% { opacity: 1; }60% { opacity: 0; }85% { opacity: 0; }}.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {position: absolute;z-index: 3;}.ace_marker-layer .ace_selection {position: absolute;z-index: 5;}.ace_marker-layer .ace_bracket {position: absolute;z-index: 6;}.ace_marker-layer .ace_error_bracket {position: absolute;border-bottom: 1px solid #DE5555;border-radius: 0;}.ace_marker-layer .ace_active-line {position: absolute;z-index: 2;}.ace_marker-layer .ace_selected-word {position: absolute;z-index: 4;box-sizing: border-box;}.ace_line .ace_fold {box-sizing: border-box;display: inline-block;height: 11px;margin-top: -2px;vertical-align: middle;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");background-repeat: no-repeat, repeat-x;background-position: center center, top left;color: transparent;border: 1px solid black;border-radius: 2px;cursor: pointer;pointer-events: auto;}.ace_dark .ace_fold {}.ace_fold:hover{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");}.ace_tooltip {background-color: #FFF;background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));border: 1px solid gray;border-radius: 1px;box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);color: black;max-width: 100%;padding: 3px 4px;position: fixed;z-index: 999999;box-sizing: border-box;cursor: default;white-space: pre;word-wrap: break-word;line-height: normal;font-style: normal;font-weight: normal;letter-spacing: normal;pointer-events: none;}.ace_folding-enabled > .ace_gutter-cell {padding-right: 13px;}.ace_fold-widget {box-sizing: border-box;margin: 0 -12px 0 1px;display: none;width: 11px;vertical-align: top;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: center;border-radius: 3px;border: 1px solid transparent;cursor: pointer;}.ace_folding-enabled .ace_fold-widget {display: inline-block;   }.ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");}.ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");}.ace_fold-widget:hover {border: 1px solid rgba(0, 0, 0, 0.3);background-color: rgba(255, 255, 255, 0.2);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);}.ace_fold-widget:active {border: 1px solid rgba(0, 0, 0, 0.4);background-color: rgba(0, 0, 0, 0.05);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);}.ace_dark .ace_fold-widget {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");}.ace_dark .ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget:hover {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);background-color: rgba(255, 255, 255, 0.1);}.ace_dark .ace_fold-widget:active {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);}.ace_inline_button {border: 1px solid lightgray;display: inline-block;margin: -1px 8px;padding: 0 5px;pointer-events: auto;cursor: pointer;}.ace_inline_button:hover {border-color: gray;background: rgba(200,200,200,0.2);display: inline-block;pointer-events: auto;}.ace_fold-widget.ace_invalid {background-color: #FFB4B4;border-color: #DE5555;}.ace_fade-fold-widgets .ace_fold-widget {transition: opacity 0.4s ease 0.05s;opacity: 0;}.ace_fade-fold-widgets:hover .ace_fold-widget {transition: opacity 0.05s ease 0.05s;opacity:1;}.ace_underline {text-decoration: underline;}.ace_bold {font-weight: bold;}.ace_nobold .ace_bold {font-weight: normal;}.ace_italic {font-style: italic;}.ace_error-marker {background-color: rgba(255, 0, 0,0.2);position: absolute;z-index: 9;}.ace_highlight-marker {background-color: rgba(255, 255, 0,0.2);position: absolute;z-index: 8;}.ace_mobile-menu {position: absolute;line-height: 1.5;border-radius: 4px;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;background: white;box-shadow: 1px 3px 2px grey;border: 1px solid #dcdcdc;color: black;}.ace_dark > .ace_mobile-menu {background: #333;color: #ccc;box-shadow: 1px 3px 2px grey;border: 1px solid #444;}.ace_mobile-button {padding: 2px;cursor: pointer;overflow: hidden;}.ace_mobile-button:hover {background-color: #eee;opacity:1;}.ace_mobile-button:active {background-color: #ddd;}.ace_placeholder {font-family: arial;transform: scale(0.9);transform-origin: left;white-space: pre;opacity: 0.7;margin: 0 10px;}
/*# sourceURL=ace/css/ace_editor.css */</style>
    <title>Online Python Compiler (Interpreter)</title>
    <link rel="shortcut icon" href="https://cdn.programiz.com/sites/tutorial2program/files/programiz-favicon_3.png" type="image/png">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0">
    <link rel="canonical" href="https://www.programiz.com/python-programming/online-compiler/">    <meta name="description" content="Write and run Python code using our online compiler (interpreter). You can use Python Shell like IDLE, and take inputs from the user in our Python compiler.">

    <!-- CMP and header ad code start -->
    <script src="./ex 8-1_files/osd.js.download"></script><script async="" src="./ex 8-1_files/apstag.js.download"></script><script type="text/javascript" async="" src="./ex 8-1_files/analytics.js.download"></script><script src="./ex 8-1_files/stub.min.js.download"></script>
    <script async="" src="./ex 8-1_files/cmp.js.download"></script>
    <script type="text/javascript">
    window.googletag = window.googletag || {};
    window.googletag.cmd = window.googletag.cmd || [];
    window.googletag.cmd.push(function () {
        window.googletag.pubads().enableAsyncRendering();
        window.googletag.pubads().disableInitialLoad();
    });
    (adsbygoogle = window.adsbygoogle || []).pauseAdRequests = 1;
    </script>
    <script>
    __tcfapi("addEventListener", 2, function(tcData, success) {
        if (success && tcData.unicLoad  === true) {
            if(!window._initAds) {
                window._initAds = true;
                var script = document.createElement('script');
                script.async = true;
                script.src = '//dsh7ky7308k4b.cloudfront.net/publishers/Programizcomnew.min.js';
                document.head.appendChild(script);			
            }

            try {
                fetch(new Request("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js", { method: 'HEAD', mode: 'no-cors' })).then(function(response) {
            return true;
            }).catch(function(e) {
            document.getElementsByClassName("content-top-ad")[0].style.display = "none";
            var ad_elements = document.getElementsByClassName("pub-ad");
            while(ad_elements.length > 0){
                ad_elements[0].parentNode.removeChild(ad_elements[0]);
            }
            var carbonScript = document.createElement("script");
            carbonScript.src = "//cdn.carbonads.com/carbon.js?serve=CKYDL27L&placement=wwwprogramizcom";
            carbonScript.id = "_carbonads_js";
            document.getElementById("carbon-block").appendChild(carbonScript);
            });
        } catch (error) {
            console.log(error);
        }
        }
    });
    </script>
    <!-- CMP and header tag ad code end -->
    
    <!-- Buy sellads CSS-->
    <style>
        #carbonads{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",Helvetica,Arial,sans-serif;--width:728px;--font-size:22px}#carbonads{display:block;overflow:hidden;max-width:var(--width);position:relative;background-color:#fcfcfc;border:solid 1px #eee;font-size:var(--font-size);box-sizing:border-box;margin:36px 0 36px 0;max-height:90px}.detail #carbonads{margin-top:12px}#carbonads a{color:inherit;text-decoration:none}#carbonads a:hover{color:inherit}.carbon-wrap{display:flex;align-items:center}carbon-img{display:block;float:left;margin:0;max-width:var(--width);line-height:1}.carbon-img img{display:block;margin:0;height:90px;width:auto}.carbon-text{display:block;float:left;padding:0 1em;line-height:1.35;max-width:calc(100% - 130px - 2em);text-align:left}.carbon-poweredby{display:block;position:absolute;bottom:0;right:0;padding:6px 10px;background:repeating-linear-gradient(-45deg,transparent,transparent 5px,hsla(0,0%,0%,.025) 5px,hsla(0,0%,0%,.025) 10px) hsla(203,11%,95%,.8);text-align:center;text-transform:uppercase;letter-spacing:.5px;font-weight:601;font-size:8px;border-top-left-radius:4px;line-height:1}@media only screen and (min-width:320px) and (max-width:759px){.carbon-text{font-size:14px}}
     </style>

    <!-- Generated using https://dns-prefetch-generator.github.io/ -->
    <meta http-equiv="x-dns-prefetch-control" content="on">
    <link rel="dns-prefetch" href="https://www.googletagservices.com/">
    <link rel="dns-prefetch" href="https://www.google-analytics.com/">
    <link rel="dns-prefetch" href="https://c.amazon-adsystem.com/">
    <link rel="dns-prefetch" href="https://dsh7ky7308k4b.cloudfront.net/">
    <link rel="dns-prefetch" href="https://securepubads.g.doubleclick.net/">
    <link rel="dns-prefetch" href="https://adservice.google.com/">
    <link rel="dns-prefetch" href="https://cdnjs.cloudflare.com/">
    <link rel="dns-prefetch" href="https://www.googletagmanager.com/">

    <link rel="stylesheet" href="./ex 8-1_files/playground.css">
    <!-- Global site tag (gtag.js) - Google Analytics -->

  <style>.unic{-webkit-font-smoothing:antialiased;line-height:1.15;-webkit-text-size-adjust:100%;box-sizing:border-box;font-family:sans-serif}.unic main{display:block}.unic h1{font-size:2em;margin:.67em 0}.unic hr{box-sizing:content-box;height:0;overflow:visible}.unic pre{font-family:monospace,monospace;font-size:1em}.unic a{background-color:transparent}.unic abbr[title]{border-bottom:none;text-decoration:underline;-webkit-text-decoration:underline dotted;text-decoration:underline dotted}.unic b,.unic strong{font-weight:bolder}.unic code,.unic kbd,.unic samp{font-family:monospace,monospace;font-size:1em}.unic small{font-size:80%}.unic sub,.unic sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}.unic sub{bottom:-.25em}.unic sup{top:-.5em}.unic img{border-style:none}.unic button,.unic input,.unic optgroup,.unic select,.unic textarea{font-family:inherit;font-size:100%;line-height:1.15;margin:0}.unic button,.unic input{overflow:visible}.unic button,.unic select{text-transform:none}.unic [type=button],.unic [type=reset],.unic [type=submit],.unic button{-webkit-appearance:button}.unic [type=button]::-moz-focus-inner,.unic [type=reset]::-moz-focus-inner,.unic [type=submit]::-moz-focus-inner,.unic button::-moz-focus-inner{border-style:none;padding:0}.unic [type=button]:-moz-focusring,.unic [type=reset]:-moz-focusring,.unic [type=submit]:-moz-focusring,.unic button:-moz-focusring{outline:1px dotted ButtonText}.unic fieldset{padding:.35em .75em .625em}.unic legend{box-sizing:border-box;color:inherit;display:table;max-width:100%;padding:0;white-space:normal}.unic progress{vertical-align:baseline}.unic textarea{overflow:auto}.unic [type=checkbox],.unic [type=radio]{box-sizing:border-box;padding:0}.unic [type=number]::-webkit-inner-spin-button,.unic [type=number]::-webkit-outer-spin-button{height:auto}.unic [type=search]{-webkit-appearance:textfield;outline-offset:-2px}.unic [type=search]::-webkit-search-decoration{-webkit-appearance:none}.unic ::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}.unic details{display:block}.unic summary{display:list-item}.unic [hidden],.unic template{display:none}.unic *,.unic :after,.unic :before{box-sizing:inherit}.unic blockquote,.unic dd,.unic dl,.unic figure,.unic h1,.unic h2,.unic h3,.unic h4,.unic h5,.unic h6,.unic hr,.unic p,.unic pre{margin:0}.unic button{background:transparent;padding:0}.unic button:focus{outline:1px dotted;outline:5px auto -webkit-focus-ring-color}.unic fieldset,.unic ol,.unic ul{margin:0;padding:0}.unic ol,.unic ul{list-style:none}.unic *{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji!important;line-height:1.5;font-weight:400;height:auto}.unic *,.unic :after,.unic :before{border:0 solid #e2e8f0}.unic hr{border-top-width:1px}.unic img{border-style:solid}.unic textarea{resize:vertical}.unic input::-webkit-input-placeholder,.unic textarea::-webkit-input-placeholder{color:#a0aec0}.unic input::-moz-placeholder,.unic textarea::-moz-placeholder{color:#a0aec0}.unic input:-ms-input-placeholder,.unic textarea:-ms-input-placeholder{color:#a0aec0}.unic input::-ms-input-placeholder,.unic textarea::-ms-input-placeholder{color:#a0aec0}.unic input::placeholder,.unic textarea::placeholder{color:#a0aec0}.unic [role=button],.unic button{cursor:pointer}.unic table{border-collapse:collapse}.unic h1,.unic h2,.unic h3,.unic h4,.unic h5,.unic h6{font-size:inherit;font-weight:inherit}.unic a{color:inherit;text-decoration:inherit}.unic button,.unic input,.unic optgroup,.unic select,.unic textarea{padding:0;line-height:inherit;color:inherit}.unic code,.unic kbd,.unic pre,.unic samp{font-family:Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace}.unic audio,.unic canvas,.unic embed,.unic iframe,.unic img,.unic object,.unic svg,.unic video{display:block;vertical-align:middle}.unic img,.unic video{max-width:100%;height:auto}.unic .container{width:100%}@media (min-width:640px){.unic .container{max-width:640px}}@media (min-width:768px){.unic .container{max-width:768px}}@media (min-width:1024px){.unic .container{max-width:1024px}}@media (min-width:1280px){.unic .container{max-width:1280px}}.unic .bg-white{background-color:#fff}.unic .bg-gray-200{background-color:#edf2f7}.unic .bg-gray-300{background-color:#e2e8f0}.unic .bg-gray-400,.unic .hover\:bg-gray-400:hover{background-color:#cbd5e0}.unic .hover\:bg-gray-600:hover{background-color:#718096}.unic .border-gray-300{border-color:#e2e8f0}.unic .rounded{border-radius:4px}.unic .rounded-full{border-radius:9999px}.unic .rounded-t-lg{border-top-left-radius:8px;border-top-right-radius:8px}.unic .rounded-b-lg{border-bottom-right-radius:8px;border-bottom-left-radius:8px}.unic .border-solid{border-style:solid}.unic .border{border-width:1px}.unic .border-t{border-top-width:1px}.unic .border-r{border-right-width:1px}.unic .border-b{border-bottom-width:1px}.unic .border-l{border-left-width:1px}.unic .cursor-pointer{cursor:pointer}.unic .block{display:block}.unic .inline{display:inline}.unic .flex{display:-webkit-box;display:flex}.unic .hidden{display:none}.unic .flex-row{-webkit-box-orient:horizontal;-webkit-box-direction:normal;flex-direction:row}.unic .flex-col{-webkit-box-orient:vertical;-webkit-box-direction:normal;flex-direction:column}.unic .flex-wrap{flex-wrap:wrap}.unic .items-center{-webkit-box-align:center;align-items:center}.unic .justify-start{-webkit-box-pack:start;justify-content:flex-start}.unic .justify-center{-webkit-box-pack:center;justify-content:center}.unic .justify-between{-webkit-box-pack:justify;justify-content:space-between}.unic .flex-1{-webkit-box-flex:1;flex:1 1 0%}.unic .flex-auto{-webkit-box-flex:1;flex:1 1 auto}.unic .font-sans{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji}.unic .font-bold{font-weight:700}.unic .h-3{height:12px}.unic .h-4{height:16px}.unic .h-5{height:20px}.unic .h-32{height:128px}.unic .h-40{height:160px}.unic .h-64{height:256px}.unic .h-full{height:100%}.unic .m-2{margin:8px}.unic .m-auto{margin:auto}.unic .mx-0{margin-left:0;margin-right:0}.unic .mx-1{margin-left:4px;margin-right:4px}.unic .mx-2{margin-left:8px;margin-right:8px}.unic .mt-2{margin-top:8px}.unic .mb-2{margin-bottom:8px}.unic .ml-4{margin-left:16px}.unic .mt-auto{margin-top:auto}.unic .ml-auto{margin-left:auto}.unic .max-h-full{max-height:100%}.unic .object-scale-down{-o-object-fit:scale-down;object-fit:scale-down}.unic .outline-none{outline:0}.unic .overflow-scroll{overflow:scroll}.unic .overflow-x-hidden{overflow-x:hidden}.unic .p-1{padding:4px}.unic .p-2{padding:8px}.unic .p-4{padding:16px}.unic .p-6{padding:24px}.unic .py-1{padding-top:4px;padding-bottom:4px}.unic .py-2{padding-top:8px;padding-bottom:8px}.unic .px-2{padding-left:8px;padding-right:8px}.unic .px-4{padding-left:16px;padding-right:16px}.unic .pb-0{padding-bottom:0}.unic .pr-2{padding-right:8px}.unic .pb-2{padding-bottom:8px}.unic .pt-4{padding-top:16px}.unic .static{position:static}.unic .fixed{position:fixed}.unic .absolute{position:absolute}.unic .relative{position:relative}.unic .inset-y-0{top:0;bottom:0}.unic .top-0{top:0}.unic .right-0{right:0}.unic .bottom-0{bottom:0}.unic .left-0{left:0}.unic .shadow{box-shadow:0 1px 3px 0 rgba(0,0,0,.1),0 1px 2px 0 rgba(0,0,0,.06)}.unic .shadow-md{box-shadow:0 4px 6px -1px rgba(0,0,0,.1),0 2px 4px -1px rgba(0,0,0,.06)}.unic .shadow-inner{box-shadow:inset 0 2px 4px 0 rgba(0,0,0,.06)}.unic .text-center{text-align:center}.unic .text-black{color:#000}.unic .text-gray-700{color:#4a5568}.unic .text-gray-800{color:#2d3748}.unic .hover\:text-white:hover{color:#fff}.unic .text-xs{font-size:12px}.unic .text-sm{font-size:14px}.unic .text-lg{font-size:18px}.unic .text-xl{font-size:20px}.unic .underline{text-decoration:underline}.unic .antialiased{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.unic .align-middle{vertical-align:middle}.unic .w-5{width:20px}.unic .w-10{width:40px}.unic .w-32{width:128px}.unic .w-1\/3{width:33.333333%}.unic .w-full{width:100%}.unic .z-40{z-index:40}.unic .z-50{z-index:50}@media (min-width:768px){.unic .md\:flex-row{-webkit-box-orient:horizontal;-webkit-box-direction:normal;flex-direction:row}.unic .md\:flex-1{-webkit-box-flex:1;flex:1 1 0%}.unic .md\:h-64{height:256px}.unic .md\:h-auto{height:auto}.unic .md\:mx-2{margin-left:8px;margin-right:8px}.unic .md\:mx-3{margin-left:12px;margin-right:12px}.unic .md\:max-w-2xl{max-width:672px}.unic .md\:pl-4{padding-left:16px}.unic .md\:text-base{font-size:16px}.unic .md\:text-xl{font-size:20px}.unic .md\:w-1\/2{width:50%}.unic .md\:w-1\/4{width:25%}}div.unic ::-webkit-scrollbar{display:none}.unic{font-size:14px;color:rgba(0,0,0,.76);-ms-overflow-style:none;overflow:auto}.unic .h24{height:24px}.unic label{width:auto}.unic .svg{height:100%}.unic :focus{outline:thin dotted}.unic-bg{background-color:hsla(0,.5%,41%,.75)}.unic .toggle__dot{top:-4px;left:-4px;-webkit-transition:all .3s ease-in-out;transition:all .3s ease-in-out}.unic input:checked~.toggle__dot{-webkit-transform:translateX(120%);transform:translateX(120%);background-color:#48bb78!important}#uniccmp{z-index:2147483639}#uniccmp-badge,.unic-badge{z-index:2147483638}.unic-badge{width:30px;height:30px;padding:5px;display:block;outline:none;position:fixed;left:10px;bottom:10px;border-radius:2px;border-radius:4px;background-image:linear-gradient(37deg,#c7c7c7,#e0e0e0);cursor:pointer}</style><script src="./ex 8-1_files/mode-python.js.download"></script><script async="" src="./ex 8-1_files/Programizcomnew.min.js.download"></script><script src="./ex 8-1_files/gpt.js.download"></script><meta http-equiv="origin-trial" content="A2shzsdPO+RKe83bUqT9oVkYwGZN6j9O7nrcOASNFPuQz8HefgVYb9qAqn6coNCSDIRtXoi6ybCrjEsYh3caFgIAAAB7eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MTM0OTU4NjgsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script src="./ex 8-1_files/pubads_impl_2021010903.js.download" async=""></script><link rel="preload" href="./ex 8-1_files/f.txt" as="script"><script type="text/javascript" src="./ex 8-1_files/f.txt"></script><link rel="preload" href="./ex 8-1_files/f(1).txt" as="script"><script type="text/javascript" src="./ex 8-1_files/f(1).txt"></script><link rel="prefetch" href="https://946c05dbf40d373690bc0703ad1b358c.safeframe.googlesyndication.com/safeframe/1-0-37/html/container.html"><link rel="prefetch" href="https://tpc.googlesyndication.com/safeframe/1-0-37/html/container.html"><link rel="preload" href="./ex 8-1_files/f.txt" as="script"><script type="text/javascript" src="./ex 8-1_files/f.txt"></script><link rel="preload" href="./ex 8-1_files/f(1).txt" as="script"><script type="text/javascript" src="./ex 8-1_files/f(1).txt"></script><link rel="preload" href="./ex 8-1_files/f.txt" as="script"><script type="text/javascript" src="./ex 8-1_files/f.txt"></script><link rel="preload" href="./ex 8-1_files/f(1).txt" as="script"><script type="text/javascript" src="./ex 8-1_files/f(1).txt"></script></head>

  <body><div id="uniccmp" data-nosnippet=""></div>
    <!-- <select id="language-changer"></select> -->
    <div class="container" id="root" data-lang="python">
      <div class="spinner" style="display: none;">
        <div class="loader"><span>{</span><span>}</span></div>
      </div>
      <div class="mobile-nav-drawer show">
        <div class="nav-backdrop">
        </div>
        <div class="nav-menu">
          <div class="nav-header-wrapper">
              <div class="nav-logo-title-wrapper">
                <a href="https://www.programiz.com/" target="_blank" class="nav-logo-link">
                  <img id="nav-logo" src="./ex 8-1_files/logo.svg">
                </a>
              </div>
            <button type="button" class="close-nav-btn" title="Close navigation">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" class="svg replaced-svg">
<path d="M19 4.85352L5.00006 18.8535" stroke="#25265E" stroke-opacity="0.7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
<path d="M5 4.85352L18.9999 18.8535" stroke="#25265E" stroke-opacity="0.7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
            </button>
          </div>
          <div class="nav-menu-list">
            <a target="_blank" href="https://www.programiz.com/python-programming/online-compiler/" class="change-lang-row python active" title="Python Online Compiler">
              <span class="change-lang-btn">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 25" class="change-lang-btn-icon svg replaced-svg">
  <path fill-opacity=".4" d="M9.091 11.663h5.782c1.61 0 2.877-1.353 2.877-2.96V3.225c0-1.559-1.315-2.73-2.886-2.99A18.088 18.088 0 0011.853 0a16.25 16.25 0 00-2.738.235c-2.45.43-2.866 1.33-2.866 2.99v2.132H12v.788H4.025C2.342 6.145.868 7.152.408 9.064c-.532 2.191-.556 3.531 0 5.82.411 1.702 1.394 2.888 3.076 2.888h1.972V15.2c0-1.9 1.672-3.538 3.635-3.538zm-.364-7.707c-.6 0-1.087-.489-1.087-1.093 0-.606.486-1.1 1.087-1.1.597 0 1.086.494 1.086 1.1a1.09 1.09 0 01-1.086 1.093zm14.83 5.108c-.416-1.665-1.21-2.919-2.895-2.919h-2.118v2.558c0 1.98-1.744 3.551-3.671 3.551H9.091c-1.584 0-2.842 1.444-2.842 3.02v5.479c0 1.558 1.338 2.475 2.868 2.923 1.833.535 3.568.632 5.76 0 1.458-.42 2.873-1.264 2.873-2.923V18.56H12v-.788h8.662c1.682 0 2.31-1.138 2.895-2.89.604-1.801.578-3.506 0-5.818zm-8.32 10.958c.6 0 1.087.488 1.087 1.093 0 .606-.486 1.1-1.087 1.1a1.095 1.095 0 01-1.086-1.1 1.09 1.09 0 011.086-1.093z"></path>
</svg>
              </span>
              <span class="nav-menu-text">
                Python Online Compiler
              </span>
            </a>
            <a target="_blank" href="https://www.programiz.com/c-programming/online-compiler/" class="change-lang-row c " title="C Online Compiler">
              <span class="change-lang-btn">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 28" class="change-lang-btn-icon svg replaced-svg">
  <path fill-opacity=".4" d="M23.903 6.916l.067-.044c-.134-.243-.334-.464-.534-.574L12.696.155C12.518.045 12.274 0 12.007 0c-.267 0-.511.066-.69.155L.646 6.32C.267 6.54 0 7.093 0 7.513v12.308c0 .243.044.508.2.752l-.044.022c.11.176.266.331.422.42l10.718 6.165c.178.11.422.154.689.154.267 0 .511-.066.69-.154l10.672-6.165c.378-.221.645-.774.645-1.194V7.491c.022-.177 0-.376-.089-.575zM12.007 19.07a5.455 5.455 0 004.736-2.74l2.869 1.68a8.794 8.794 0 01-7.605 4.374c-4.847 0-8.783-3.91-8.783-8.728 0-4.817 3.936-8.728 8.783-8.728a8.796 8.796 0 017.627 4.42l-2.89 1.656a5.43 5.43 0 00-4.737-2.762c-3.002 0-5.448 2.431-5.448 5.414 0 2.983 2.446 5.414 5.448 5.414z"></path>
</svg>
              </span>
              <span class="nav-menu-text">
                C Online Compiler
              </span>
            </a>
            <a target="_blank" href="https://www.programiz.com/cpp-programming/online-compiler/" class="change-lang-row cpp " title="C++ Online Compiler">
              <span class="change-lang-btn">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 27" class="change-lang-btn-icon svg replaced-svg">
  <path fill="#25265E" fill-opacity=".4" d="M23.903 6.639l.067-.043c-.134-.233-.334-.445-.534-.551L12.696.148C12.518.042 12.274 0 12.007 0a1.64 1.64 0 00-.69.148L.646 6.066C.267 6.278 0 6.808 0 7.21v11.814c0 .233.044.488.2.72l-.044.022c.11.17.266.318.422.403l10.718 5.918c.178.106.422.148.689.148.267 0 .511-.064.69-.148l10.672-5.918c.378-.212.645-.742.645-1.145V7.19c.022-.17 0-.36-.089-.551zm-7.893 6.893v-.849h1.111v-1.06h1.112v1.06h1.112v.849h-1.112v1.06h-1.112v-1.06H16.01zm.733-2.97c-.934-1.59-2.712-2.65-4.736-2.65-3.002 0-5.448 2.332-5.448 5.195 0 2.864 2.446 5.197 5.448 5.197 2.024 0 3.802-1.06 4.736-2.63l2.869 1.612c-1.512 2.502-4.358 4.2-7.605 4.2-4.847 0-8.783-3.755-8.783-8.379 0-4.623 3.936-8.377 8.783-8.377 3.269 0 6.115 1.718 7.627 4.242l-2.89 1.59zm6.604 2.97h-1.112v1.06h-.889v-1.06h-1.334v-.849h1.334v-1.06h.89v1.06h1.111v.849z"></path>
</svg>
              </span>
              <span class="nav-menu-text">
                C++ Online Compiler
              </span>
            </a>
          </div>
        </div>
      </div>

      <div class="wrapper" style="display: block;">
        <div class="header">
          <div class="header-wrapper">
            <div class="burger-menu">
              <button type="button" class="burger-menu-btn" title="Open navigation">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" class="svg burger-menu-btn-icon replaced-svg">
  <path d="M3 12H21" stroke="#25265E" stroke-opacity="0.7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
  <path d="M3 6H21" stroke="#25265E" stroke-opacity="0.7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
  <path d="M3 18H21" stroke="#25265E" stroke-opacity="0.7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
              </button>
            </div>
            <div class="logo-wrapper">
              <h1 class="logo-title-wrapper">
                <a href="https://www.programiz.com/" target="_blank" class="logo-link">
                  <img id="logo" src="./ex 8-1_files/logo.svg">
                  <span class="logo-sub-title-wrapper">
                    <span class="logo-sub-title">Python Online Compiler</span>
                  </span>
                </a>
              </h1>
            </div>
          </div>
          <div class="compiler-header-ad">
            <div id="div-gpt-ad-Programizcom36786" class="content-top-ad" data-google-query-id="CJKMqJLimO4CFZvUcwEdH1UIfQ">
            <div id="google_ads_iframe_/8095840/.2_A.36786.3_Programiz.com_tier1_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/8095840/.2_A.36786.3_Programiz.com_tier1_0" title="3rd party ad content" name="google_ads_iframe_/8095840/.2_A.36786.3_Programiz.com_tier1_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" style="border: 0px; vertical-align: bottom;" data-google-container-id="r" data-load-complete="true" src="./ex 8-1_files/saved_resource.html"></iframe></div></div>

            <!-- buysell ads -->
                <div class="compiler-header-ad" id="carbon-block"></div>

          </div>
          <div id="add-replacement"></div>
          <div id="feedback-desktop">
            <a id="ad-link" href="https://app.programiz.com/app-compiler">&nbsp;Learn Python App</a>
          </div>
          <div id="feedback-mobile">
            <a id="mobile-ad-link" href="https://app.programiz.com/app-compiler">&nbsp;Learn Python</a>
          </div>
        </div>
        <div class="mobile-top-bar clearfix">
          <div class="options-wrapper">
            <div id="back-button" class="options-item-wrapper clearfix">
              <svg xmlns="http://www.w3.org/2000/svg" width="17" height="14" viewBox="0 0 17 14" fill="none" class="svg options-item replaced-svg">
<path d="M6.05625 13.3906C6.38169 13.716 6.90933 13.716 7.23476 13.3906L7.51458 13.1107C7.84002 12.7853 7.84002 12.2577 7.51458 11.9322L3.83301 8.25065C3.75613 8.17377 3.81058 8.04232 3.9193 8.04232L15.4997 8.04232C15.9599 8.04232 16.333 7.66922 16.333 7.20898L16.333 6.79232C16.333 6.33208 15.9599 5.95898 15.4997 5.95898L3.9193 5.95898C3.81058 5.95898 3.75613 5.82753 3.83301 5.75065L7.51459 2.06907C7.84002 1.74364 7.84002 1.216 7.51459 0.890562L7.23476 0.61074C6.90933 0.285303 6.38169 0.285303 6.05625 0.610739L0.255598 6.41139C-0.0698398 6.73683 -0.0698398 7.26447 0.255598 7.5899L6.05625 13.3906Z" fill="#25265E" fill-opacity="0.4"></path>
</svg>
            </div>
          </div>
          <div class="pills-wrapper">
            <div class="pills clearfix">
              <button class="pill active compiler-pill">
                main.py              </button>
              <button class="pill shell-pill">
                Shell              </button>
            </div>
          </div>
          <div class="other-options-wrapper">
            <!-- <div id="feedback-mobile" class="options-item-wrapper">
              <a href="https://programiz.com/contact" class="options-item">
                <img class="svg" src="assets/icons/message-square.svg" />
              </a>
            </div> -->
            <div id="toggle-dark-mode-mobile" class="options-item-wrapper clearfix">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="toggle-dark-mode-mobile-icon moon svg options-item replaced-svg">
  <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
</svg>
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="toggle-dark-mode-mobile-icon sun svg options-item replaced-svg">
  <circle cx="12" cy="12" r="5"></circle>
  <line x1="12" y1="1" x2="12" y2="3"></line>
  <line x1="12" y1="21" x2="12" y2="23"></line>
  <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
  <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
  <line x1="1" y1="12" x2="3" y2="12"></line>
  <line x1="21" y1="12" x2="23" y2="12"></line>
  <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
  <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
</svg>
            </div>
          </div>
        </div>
        <div class="sidebar-wrapper">
          <a target="_blank" href="https://www.programiz.com/python-programming/online-compiler/" class="change-lang-btn python active" title="Online Python Compiler">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 25" class="change-lang-btn-icon svg replaced-svg">
  <path fill-opacity=".4" d="M9.091 11.663h5.782c1.61 0 2.877-1.353 2.877-2.96V3.225c0-1.559-1.315-2.73-2.886-2.99A18.088 18.088 0 0011.853 0a16.25 16.25 0 00-2.738.235c-2.45.43-2.866 1.33-2.866 2.99v2.132H12v.788H4.025C2.342 6.145.868 7.152.408 9.064c-.532 2.191-.556 3.531 0 5.82.411 1.702 1.394 2.888 3.076 2.888h1.972V15.2c0-1.9 1.672-3.538 3.635-3.538zm-.364-7.707c-.6 0-1.087-.489-1.087-1.093 0-.606.486-1.1 1.087-1.1.597 0 1.086.494 1.086 1.1a1.09 1.09 0 01-1.086 1.093zm14.83 5.108c-.416-1.665-1.21-2.919-2.895-2.919h-2.118v2.558c0 1.98-1.744 3.551-3.671 3.551H9.091c-1.584 0-2.842 1.444-2.842 3.02v5.479c0 1.558 1.338 2.475 2.868 2.923 1.833.535 3.568.632 5.76 0 1.458-.42 2.873-1.264 2.873-2.923V18.56H12v-.788h8.662c1.682 0 2.31-1.138 2.895-2.89.604-1.801.578-3.506 0-5.818zm-8.32 10.958c.6 0 1.087.488 1.087 1.093 0 .606-.486 1.1-1.087 1.1a1.095 1.095 0 01-1.086-1.1 1.09 1.09 0 011.086-1.093z"></path>
</svg>
          </a>
          <a target="_blank" href="https://www.programiz.com/c-programming/online-compiler/" class="change-lang-btn c " title="Online C Compiler">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 28" class="change-lang-btn-icon svg replaced-svg">
  <path fill-opacity=".4" d="M23.903 6.916l.067-.044c-.134-.243-.334-.464-.534-.574L12.696.155C12.518.045 12.274 0 12.007 0c-.267 0-.511.066-.69.155L.646 6.32C.267 6.54 0 7.093 0 7.513v12.308c0 .243.044.508.2.752l-.044.022c.11.176.266.331.422.42l10.718 6.165c.178.11.422.154.689.154.267 0 .511-.066.69-.154l10.672-6.165c.378-.221.645-.774.645-1.194V7.491c.022-.177 0-.376-.089-.575zM12.007 19.07a5.455 5.455 0 004.736-2.74l2.869 1.68a8.794 8.794 0 01-7.605 4.374c-4.847 0-8.783-3.91-8.783-8.728 0-4.817 3.936-8.728 8.783-8.728a8.796 8.796 0 017.627 4.42l-2.89 1.656a5.43 5.43 0 00-4.737-2.762c-3.002 0-5.448 2.431-5.448 5.414 0 2.983 2.446 5.414 5.448 5.414z"></path>
</svg>
          </a>
          <a target="_blank" href="https://www.programiz.com/cpp-programming/online-compiler/" class="change-lang-btn cpp " title="Online C++ Compiler">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 27" class="change-lang-btn-icon svg replaced-svg">
  <path fill="#25265E" fill-opacity=".4" d="M23.903 6.639l.067-.043c-.134-.233-.334-.445-.534-.551L12.696.148C12.518.042 12.274 0 12.007 0a1.64 1.64 0 00-.69.148L.646 6.066C.267 6.278 0 6.808 0 7.21v11.814c0 .233.044.488.2.72l-.044.022c.11.17.266.318.422.403l10.718 5.918c.178.106.422.148.689.148.267 0 .511-.064.69-.148l10.672-5.918c.378-.212.645-.742.645-1.145V7.19c.022-.17 0-.36-.089-.551zm-7.893 6.893v-.849h1.111v-1.06h1.112v1.06h1.112v.849h-1.112v1.06h-1.112v-1.06H16.01zm.733-2.97c-.934-1.59-2.712-2.65-4.736-2.65-3.002 0-5.448 2.332-5.448 5.195 0 2.864 2.446 5.197 5.448 5.197 2.024 0 3.802-1.06 4.736-2.63l2.869 1.612c-1.512 2.502-4.358 4.2-7.605 4.2-4.847 0-8.783-3.755-8.783-8.379 0-4.623 3.936-8.377 8.783-8.377 3.269 0 6.115 1.718 7.627 4.242l-2.89 1.59zm6.604 2.97h-1.112v1.06h-.889v-1.06h-1.334v-.849h1.334v-1.06h.89v1.06h1.111v.849z"></path>
</svg>
          </a>
        </div>
        <div class="editor-wrapper">
          <div class="editor-desktop-top-bar">
            <div class="file-name">main.py</div>
            <div class="desktop-top-bar__btn-wrapper">
              <button type="button" id="toggle-expanded-mode-desktop" title="Enter Fullscreen">
                <svg xmlns="http://www.w3.org/2000/svg" fill="rgba(37, 38, 94, 0.7)" viewBox="0 0 16 16" width="18" height="18" class="toggle-expanded-mode-mobile-icon expand svg replaced-svg">
  <path d="M5.038 2.22a.889.889 0 000-1.778v1.777zM.445 5.033a.889.889 0 101.778 0H.445zm13.334 0a.889.889 0 001.777 0H13.78zM10.964.44a.889.889 0 000 1.778V.441zm0 13.334a.889.889 0 000 1.778v-1.778zm4.592-2.815a.889.889 0 00-1.777 0h1.777zm-13.333 0a.889.889 0 00-1.778 0h1.778zm2.815 4.593a.889.889 0 000-1.778v1.778zm0-15.111H2.815v1.777h2.223V.442zm-2.223 0a2.37 2.37 0 00-2.37 2.37h1.778c0-.327.265-.593.592-.593V.442zm-2.37 2.37v2.222h1.778V2.812H.445zm15.111 2.222V2.812H13.78v2.222h1.777zm0-2.222a2.37 2.37 0 00-2.37-2.37v1.777c.327 0 .593.265.593.593h1.777zm-2.37-2.37h-2.222v1.777h2.222V.441zm-2.222 15.11h2.222v-1.777h-2.222v1.778zm2.222 0a2.37 2.37 0 002.37-2.37H13.78a.593.593 0 01-.593.593v1.778zm2.37-2.37V10.96H13.78v2.222h1.777zM.446 10.96v2.222h1.777V10.96H.445zm0 2.222a2.37 2.37 0 002.37 2.37v-1.777a.593.593 0 01-.593-.593H.445zm2.37 2.37h2.222v-1.777H2.816v1.778z" fill-opacity=".7"></path>
</svg>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="18" height="18" fill="rgba(37, 38, 94, 0.7)" class="toggle-expanded-mode-mobile-icon minimize hidden svg replaced-svg">
  <path fill="#25265E" fill-opacity=".7" d="M5.926 1.334a.889.889 0 10-1.778 0h1.778zM1.333 4.15a.889.889 0 100 1.778V4.149zm13.334 1.778a.889.889 0 000-1.778v1.778zm-2.815-4.593a.889.889 0 00-1.778 0h1.778zm-1.778 13.334a.889.889 0 001.778 0h-1.778zm4.593-2.815a.889.889 0 000-1.778v1.778zM1.334 10.075a.889.889 0 000 1.778v-1.778zm2.814 4.593a.889.889 0 001.778 0H4.148zm0-13.334v2.223h1.778V1.334H4.148zm0 2.223a.593.593 0 01-.592.592v1.778a2.37 2.37 0 002.37-2.37H4.148zm-.592.592H1.333v1.778h2.223V4.149zm11.11 0h-2.221v1.778h2.222V4.149zm-2.221 0a.593.593 0 01-.593-.593h-1.778a2.37 2.37 0 002.37 2.37V4.15zm-.593-.593V1.334h-1.778v2.222h1.778zm0 11.112v-2.222h-1.778v2.222h1.778zm0-2.222c0-.328.265-.593.593-.593v-1.778a2.37 2.37 0 00-2.37 2.37h1.777zm.593-.593h2.222v-1.778h-2.222v1.778zm-11.111 0h2.222v-1.778H1.334v1.778zm2.222 0c.327 0 .592.265.592.593h1.778a2.37 2.37 0 00-2.37-2.37v1.777zm.592.593v2.222h1.778v-2.222H4.148z"></path>
</svg>
              </button>
              <button type="button" id="toggle-dark-mode-desktop" title="Toggle dark mode">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="toggle-dark-mode-mobile-icon moon svg replaced-svg">
  <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
</svg>
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="toggle-dark-mode-mobile-icon sun svg replaced-svg">
  <circle cx="12" cy="12" r="5"></circle>
  <line x1="12" y1="1" x2="12" y2="3"></line>
  <line x1="12" y1="21" x2="12" y2="23"></line>
  <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
  <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
  <line x1="1" y1="12" x2="3" y2="12"></line>
  <line x1="21" y1="12" x2="23" y2="12"></line>
  <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
  <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
</svg>
              </button>
              <button class="desktop-run-button run">
                &nbsp;Run&nbsp;
              </button>
            </div>
          </div>
          <button class="mobile-run-button run">
            Run
          </button>
          <div id="editor" class=" ace_editor ace-tm" style="font-family: droid_sans_monoregular; font-size: 14px; line-height: 22px; height: 110px;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px; height: 1px; width: 1px; top: 109px; left: 46px;"></textarea><div class="ace_gutter" aria-hidden="true" style="left: 0px; width: 42px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px; top: 0px; left: 0px; width: 42px;"><div class="ace_gutter-cell " style="height: 22px; top: 0px;">1<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 22px; top: 22px;">2<span style="display: none; height: 22px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 22px; top: 44px;">3<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 22px; top: 66px;">4<span style="display: none;"></span></div><div class="ace_gutter-cell ace_gutter-active-line " style="height: 22px; top: 88px;">5<span style="display: none;"></span></div></div></div><div class="ace_scroller" style="line-height: 22px; left: 42px; right: 0px; bottom: 0px;"><div class="ace_content" style="top: 0px; left: 0px; width: 463px; height: 154px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 676px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_selection ace_br1 ace_start" style="height: 22px; right: 0px; top: 0px; left: 4px;"></div><div class="ace_selection ace_br12" style="height: 22px; width: 0px; top: 88px; left: 4px;"></div><div class="ace_selection ace_br8" style="height: 66px; right: 0px; top: 22px; left: 4px;"></div></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px; top: 0px; left: 0px;"><div class="ace_line_group" style="height: 22px; top: 0px;"><div class="ace_line" style="height: 22px;"><span class="ace_identifier">s</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_string">'sadhana'</span></div></div><div class="ace_line_group" style="height: 22px; top: 22px;"><div class="ace_line" style="height: 22px;"><span class="ace_keyword">print</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">s</span><span class="ace_paren ace_rparen">)</span></div></div><div class="ace_line_group" style="height: 22px; top: 44px;"><div class="ace_line" style="height: 22px;"><span class="ace_identifier">r</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">s</span><span class="ace_paren ace_lparen">[</span><span class="ace_punctuation">::</span><span class="ace_keyword ace_operator">-</span><span class="ace_constant ace_numeric">1</span><span class="ace_paren ace_rparen">]</span></div></div><div class="ace_line_group" style="height: 22px; top: 66px;"><div class="ace_line" style="height: 22px;"><span class="ace_keyword">print</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">r</span><span class="ace_paren ace_rparen">)</span></div></div><div class="ace_line_group" style="height: 22px; top: 88px;"><div class="ace_line" style="height: 22px;"></div></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor" style="display: block; top: 88px; left: 4px; width: 8px; height: 22px; animation-duration: 1000ms;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 21px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 21px; height: 110px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="height: 21px; left: 42px; right: 0px; display: none;"><div class="ace_scrollbar-inner" style="height: 21px; width: 463px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>
        </div>

        <div class="terminal-wrapper">
          <div class="terminal-desktop-top-bar">
            <div class="shell-name">
              Shell            </div>
            <div class="terminal-desktop-top-bar__btn-wrapper">
              <button class="desktop-clear-button">
                  &nbsp;Clear&nbsp;
              </button>
            </div>
          </div>
          <div id="terminal" class=" ace_editor ace-tm" style="font-family: droid_sans_monoregular; font-size: 14px; line-height: 22px; height: 66px;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px; height: 1px; width: 1px; top: 65px; left: 21px;"></textarea><div class="ace_gutter" aria-hidden="true" style="display: none; left: 0px; width: 42px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px; top: 0px; left: 0px; width: 42px;"><div class="ace_gutter-cell " style="height: 22px; top: 0px;">1<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 22px; top: 22px;">2<span style="display: none;"></span></div><div class="ace_gutter-cell ace_gutter-active-line " style="height: 22px; top: 44px;">3<span style="display: none;"></span></div></div></div><div class="ace_scroller" style="line-height: 22px; left: 0px; right: 0px; bottom: 0px;"><div class="ace_content" style="top: 0px; left: 0px; width: 505px; height: 110px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 676px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px; top: 0px; left: 0px;"><div class="ace_line_group" style="height: 22px; top: 0px;"><div class="ace_line" style="height: 22px;">sadhana</div></div><div class="ace_line_group" style="height: 22px; top: 22px;"><div class="ace_line" style="height: 22px;">anahdas</div></div><div class="ace_line_group" style="height: 22px; top: 44px;"><div class="ace_line" style="height: 22px;"><span class="ace_comment ace_line ace_colons ace_dosbatch">&gt;</span> </div></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_slim-cursors ace_hidden-cursors"><div class="ace_cursor" style="display: block; top: 44px; left: 21px; width: 8px; height: 22px; animation-duration: 1000ms;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 21px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 21px; height: 66px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 21px; left: 0px; right: 0px;"><div class="ace_scrollbar-inner" style="height: 21px; width: 505px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>
        </div>
      </div>
    </div>

    <script defer="" type="text/javascript">

      var playStoreUrl =
          "https://play.google.com/store/apps/details?id=com.programiz.learnpython",
        appStoreUrl =
          "https://apps.apple.com/app/apple-store/id1472188189?pt=120228772",
        desktopUrl = "https://www.programiz.com/learn-python";

      var os, a;

      a = document.getElementById("ad-link");
      b = document.getElementById("mobile-ad-link");

      a.href = "https://app.programiz.com/app-compiler";
      b.href = "https://app.programiz.com/app-compiler";
    </script><iframe name="__tcfapiLocator" style="display: none;" src="./ex 8-1_files/saved_resource(1).html"></iframe><iframe name="__uspapiLocator" style="display: none;" src="./ex 8-1_files/saved_resource(2).html"></iframe>
    <!-- The use of the cloudflare cdn for all external libraries is intential. We are trying to reduce the number
         of DNS lookups.
    -->
    <script defer="" src="./ex 8-1_files/socket.io.min.js.download"></script>
    <script defer="" src="./ex 8-1_files/jquery.min.js.download"></script>

    <script defer="" src="./ex 8-1_files/ace.js.download"></script>
    <script defer="" src="./ex 8-1_files/mousetrap.min.js.download"></script>
    <script defer="" src="./ex 8-1_files/final.js.download"></script>
    <script defer="" src="./ex 8-1_files/js"></script>
    <script defer="">
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());

      gtag("config", "UA-36675496-1");
    </script>
  

<iframe src="./ex 8-1_files/iu3.html" style="display: none;"></iframe><iframe id="google_osd_static_frame_6241493316977" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;" src="./ex 8-1_files/saved_resource(3).html"></iframe></body><iframe sandbox="allow-scripts allow-same-origin" id="4716d6cca915afb" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./ex 8-1_files/pd.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="484bf322ac03a7c" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./ex 8-1_files/ixmatch.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="498aba01af3f825" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./ex 8-1_files/usync.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="50daf1303770e76" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./ex 8-1_files/async_usersync.html">
    </iframe><iframe sandbox="allow-scripts allow-same-origin" id="51b5452fca1c6c8" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./ex 8-1_files/check.html">
    </iframe></html>