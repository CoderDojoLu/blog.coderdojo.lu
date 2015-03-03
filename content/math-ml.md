Title: MathML? Good Idea :)
Date: 2014-08-22 07:20
Modified: 2014-08-22 07:21
Category: math
Tags: math, web, html, markup, mathml, xml
Slug: math-ml
Lang: en
Email: steve@localhost.lu
Author: Steve Clement
Summary: Ever wondered how to include Math in your blog posts or on your website? MathML!

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"> 
  <mrow>
    <mi>x</mi>
    <mo>=</mo>
    <mfrac>
      <mrow>
        <mo>&#x2212;</mo>
        <mi>b</mi>
        <mo>&#xB1;</mo>
        <msqrt>
          <mrow>
            <msup>
              <mi>b</mi>
              <mn>2</mn>
            </msup>
            <mo>&#x2212;</mo>
            <mn>4</mn>
            <mi>a</mi>
            <mi>c</mi>
          </mrow>
        </msqrt>
      </mrow>
      <mrow>
        <mn>2</mn>
        <mi>a</mi>
      </mrow>
    </mfrac>
  </mrow>
</math>

See the above, this is all MathML Magic and when we take a look at the source, plain text:

``` xml
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mrow>
    <mi>x</mi>
    <mo>=</mo>
    <mfrac>
      <mrow>
        <mo>&#x2212;</mo>
        <mi>b</mi>
        <mo>&#xB1;</mo>
        <msqrt>
          <mrow>
            <msup>
              <mi>b</mi>
              <mn>2</mn>
            </msup>
            <mo>&#x2212;</mo>
            <mn>4</mn>
            <mi>a</mi>
            <mi>c</mi>
          </mrow>
        </msqrt>
      </mrow>
      <mrow>
        <mn>2</mn>
        <mi>a</mi>
      </mrow>
    </mfrac>
  </mrow>
</math>
```


Yeah, quite complex, let us take the amazing <a href="https://en.wikipedia.org/wiki/Pythagorean_theorem">Pythagorean theorem</a>:

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"> 
  <mrow>
    <msup><mi>a</mi><mn>2</mn></msup>
    <mo>+</mo>
    <msup><mi>b</mi><mn>2</mn></msup>
    <mo>=</mo>
    <msup><mi>c</mi><mn>2</mn></msup>
  </mrow>
</math>

The code would look like this:

``` xml
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"> 
  <mrow>
    <msup><mi>a</mi><mn>2</mn></msup>
    <mo>+</mo>
    <msup><mi>b</mi><mn>2</mn></msup>
    <mo>=</mo>
    <msup><mi>c</mi><mn>2</mn></msup>
  </mrow>
</math>
```

If you want more examples <a href="http://www.w3.org/TR/MathML/chapter1.html#intro.example" target="_blank">click here</a> for the <a href="https://en.wikipedia.org/wiki/World_Wide_Web_Consortium" target="_blank">W3C</a> ones.

Stay :yin_yang: and keep coding :)
