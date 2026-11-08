import re

def fix_pdf_modal(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update variables
    content = content.replace(
        "let isDrawing = false;\n    let strokeCount = 0;\n    let lastX = 0;\n    let lastY = 0;",
        "let isDrawing = false;\n    let strokeCount = 0;\n    let pointsDrawn = 0;\n    let hasSigned = false;\n    let lastX = 0;\n    let lastY = 0;"
    )

    # 2. Update setupCanvasDpi
    old_setup = """    function setupCanvasDpi() {
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = rect.width * dpr;
      canvas.height = rect.height * dpr;
      ctx.scale(dpr, dpr);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#ffffff'; // Pure white ink on solid black
    }"""

    new_setup = """    function setupCanvasDpi() {
      const rect = canvas.getBoundingClientRect();
      const dpr = Math.max(window.devicePixelRatio || 1, 1);
      const cssW = (rect.width > 20) ? rect.width : (canvas.parentElement ? canvas.parentElement.clientWidth : 540);
      const cssH = (rect.height > 20) ? rect.height : 140;

      canvas.width = Math.round(cssW * dpr);
      canvas.height = Math.round(cssH * dpr);
      canvas.style.width = cssW + 'px';
      canvas.style.height = cssH + 'px';

      ctx.resetTransform ? ctx.resetTransform() : ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.scale(dpr, dpr);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#ffffff';
    }"""
    if old_setup in content:
        content = content.replace(old_setup, new_setup)
    else:
        print("Note: old_setup not found verbatim in", path)

    # 3. Replace drawing block
    old_draw_block = """    // Canvas Drawing Handlers (Touch & Mouse)
    function getCanvasCoords(e) {
      const rect = canvas.getBoundingClientRect();
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      const clientY = e.touches ? e.touches[0].clientY : e.clientY;
      return {
        x: clientX - rect.left,
        y: clientY - rect.top
      };
    }

    function startDraw(e) {
      isDrawing = true;
      strokeCount++;
      if (placeholder) placeholder.classList.add('hidden');
      const coords = getCanvasCoords(e);
      lastX = coords.x;
      lastY = coords.y;
      ctx.beginPath();
      ctx.moveTo(coords.x, coords.y);
    }

    function draw(e) {
      if (!isDrawing) return;
      e.preventDefault();
      const coords = getCanvasCoords(e);
      ctx.lineTo(coords.x, coords.y);
      ctx.stroke();
      lastX = coords.x;
      lastY = coords.y;
    }

    function stopDraw() {
      if (isDrawing) {
        isDrawing = false;
        ctx.closePath();
      }
    }

    canvas.addEventListener('mousedown', startDraw);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDraw);
    canvas.addEventListener('mouseleave', stopDraw);

    canvas.addEventListener('touchstart', (e) => {
      e.preventDefault();
      startDraw(e);
    }, { passive: false });
    canvas.addEventListener('touchmove', draw, { passive: false });
    canvas.addEventListener('touchend', stopDraw);

    if (btnClearSig) {
      btnClearSig.addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        strokeCount = 0;
        if (placeholder) placeholder.classList.remove('hidden');
      });
    }"""

    new_draw_block = """    // Canvas Drawing Handlers (High-Precision Pointer, Touch & Mouse)
    function getCanvasCoords(e) {
      const rect = canvas.getBoundingClientRect();
      let clientX = e.clientX;
      let clientY = e.clientY;
      if ((clientX === undefined || clientY === undefined) && e.touches && e.touches.length > 0) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
      } else if ((clientX === undefined || clientY === undefined) && e.changedTouches && e.changedTouches.length > 0) {
        clientX = e.changedTouches[0].clientX;
        clientY = e.changedTouches[0].clientY;
      }
      return {
        x: (clientX !== undefined ? clientX : 0) - rect.left,
        y: (clientY !== undefined ? clientY : 0) - rect.top
      };
    }

    function startDraw(e) {
      isDrawing = true;
      strokeCount++;
      pointsDrawn++;
      hasSigned = true;
      if (placeholder) placeholder.classList.add('hidden');

      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#ffffff';

      const coords = getCanvasCoords(e);
      lastX = coords.x;
      lastY = coords.y;
      ctx.beginPath();
      ctx.moveTo(coords.x, coords.y);
    }

    function draw(e) {
      if (!isDrawing) return;
      if (e.cancelable && (e.type.startsWith('touch') || e.type.startsWith('pointer'))) {
        e.preventDefault();
      }
      pointsDrawn++;
      hasSigned = true;
      const coords = getCanvasCoords(e);
      ctx.lineTo(coords.x, coords.y);
      ctx.stroke();
      lastX = coords.x;
      lastY = coords.y;
    }

    function stopDraw() {
      if (isDrawing) {
        isDrawing = false;
        ctx.closePath();
      }
    }

    if (window.PointerEvent) {
      canvas.addEventListener('pointerdown', (e) => {
        try { canvas.setPointerCapture(e.pointerId); } catch (_) {}
        startDraw(e);
      });
      canvas.addEventListener('pointermove', draw);
      canvas.addEventListener('pointerup', (e) => {
        try { canvas.releasePointerCapture(e.pointerId); } catch (_) {}
        stopDraw();
      });
      canvas.addEventListener('pointercancel', stopDraw);
      canvas.addEventListener('pointerleave', stopDraw);
    } else {
      canvas.addEventListener('mousedown', startDraw);
      canvas.addEventListener('mousemove', draw);
      canvas.addEventListener('mouseup', stopDraw);
      canvas.addEventListener('mouseleave', stopDraw);

      canvas.addEventListener('touchstart', (e) => {
        if (e.cancelable) e.preventDefault();
        startDraw(e);
      }, { passive: false });
      canvas.addEventListener('touchmove', draw, { passive: false });
      canvas.addEventListener('touchend', stopDraw);
      canvas.addEventListener('touchcancel', stopDraw);
    }

    if (btnClearSig) {
      btnClearSig.addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        strokeCount = 0;
        pointsDrawn = 0;
        hasSigned = false;
        if (placeholder) placeholder.classList.remove('hidden');
      });
    }"""

    if old_draw_block in content:
        content = content.replace(old_draw_block, new_draw_block)
        print("Replaced draw block in", path)
    else:
        print("Warning: old_draw_block not matched in", path)

    # 4. Replace validation
    old_val = """        if (strokeCount < 3) {
          alert(t.errSig);
          return;
        }"""

    new_val = """        // Validate digital signature (accepts 1 or more strokes with genuine drawn points/pixels)
        let isSigValid = false;
        if (hasSigned && (pointsDrawn >= 1 || strokeCount >= 1)) {
          try {
            const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const d = imgData.data;
            let nonZero = 0;
            for (let i = 3; i < d.length; i += 16) {
              if (d[i] > 10) {
                nonZero++;
                if (nonZero >= 5) {
                  isSigValid = true;
                  break;
                }
              }
            }
          } catch (_) {
            isSigValid = (hasSigned && (pointsDrawn >= 1 || strokeCount >= 1));
          }
        }

        if (!isSigValid) {
          alert(t.errSig);
          return;
        }"""

    if old_val in content:
        content = content.replace(old_val, new_val)
        print("Replaced signature validation in", path)
    else:
        print("Warning: old_val not matched in", path)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done fixing", path)

fix_pdf_modal('app/pdf-modal.js')
fix_pdf_modal('pdf-modal.js')
