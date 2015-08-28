/*C4 = 261.63 Hz
C#4 = 277.18 Hz
D4 = 293.66 Hz
D#4 = 311.13 Hz
E4 = 329.63 Hz
F4 = 349.23 Hz
F#4 = 369.99 Hz
G4 = 392 Hz
G#4 = 415.3 Hz
A4 = 440 Hz
A#4 = 466.16 Hz
B4 = 493.88 Hz */

/*var notes = {
"C4" = 261.63,
"C#4" = 277.18,
"D4" = 293.66,
"D#4" = 311.13,
"E4" = 329.63,
"F4" = 349.23,
"F#4" = 369.99,
"G4" = 392.0,
"G#4" = 415.3,
"A4" = 440.0,
"A#4" = 466.16,
"B4" = 493.88};*/


function play_tone(freq,color) {
 
    var samples = [];
    var samples_length = 1 * 44100;            // 1 second (44.1 KHz)
    for (var i=0; i<samples_length; i++) { // fills array with samples
        var t = i/samples_length;            // time from 0 to 1
        // Generate samples using sine wave equation (between 0 and 255)
        samples[i] = 128+Math.round(127*Math.sin(freq*2*Math.PI*t));
//        samples[i] *= (1-t); // fade effect
    }

    var wave = new RIFFWAVE();                  // Create raw wav file
    wave.header.sampleRate = samples_length;    // 44.1Khz (1 second)
    wave.header.numChannels = 1;                // 1 channel (mono)
    wave.Make(samples);

    var audio = new Audio();    // Create <audio> tag
    audio.src=wave.dataURI;
    audio.play();
}

$(document).ready(function(){


    $("a#btn-play").click(function(){
        var btn = $(this);
        $('div#colorLayer').css('background-color',btn.attr('color'));
        $('div#colorLayer').show(0,function(){
            play_tone(btn.attr('freq'),btn.attr('color'));
            $('div#colorLayer').delay(3000).hide(2000);
        });
    });



});
