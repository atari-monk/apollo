# Draw sprite on Canvas

[Up](index.md)
[Main](../../../../index.md)

```typescript
draw(ctx) {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.angle);
        const sx = this.currentFrame * this.frameWidth;
        ctx.drawImage(
            this.image,
            sx,
            0,
            this.frameWidth,
            this.frameHeight,
            -this.frameWidth / 2,
            -this.frameHeight / 2,
            this.frameWidth,
            this.frameHeight
        );
        ctx.restore();
    }
```

[Up](index.md)
[Main](../../../../index.md)
