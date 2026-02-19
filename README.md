# Regular Manim render 
Just render the multimedia file using

```
    manim *args <file.py> <Scene>
```

where `*args`:
    - `-p` for autoplay after render
    - `-ql` or `-qh` for low or high render quality

# Manim-Slides

You must include, at least `from manim_slides import Slide` in the `.py` file. Then you must use `self.next_slide(loop = <bool>)` to mark when one slide starts and another ends. Note that this DOES NOT remove anything from screen. It just adds keyframes for the controls.
Once everyting is finished, just render the file using `manim-slides`

```
    manim-slides render <example.py> <Scene>
```

Finally convert then to `html` compatible with any modern web browser using 
```
    manim-slides convert <Scene> <file.html> -ccontrols=true
```
Remove `-ccontrols=true` for no visible controls or add `--one-file` and `--offline` to get a single file with all the needed data so it can be just copied, transferd and opened.

## References

[Manim Community Edition](https://docs.manim.community/en/stable/)

[Manim Slides](https://manim-slides.eertmans.be/latest/index.html)