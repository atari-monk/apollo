# Note Api Array

[Up](index.md)
[Main](../../../../index.md)

-   This is a mock api that uses array as storage.

```typescript
import { Injectable } from "@nestjs/common";
import { Note } from "./note.interface";

@Injectable()
export class NotesService {
    private notes: Note[] = [];

    create(note: Note): Note {
        note.id = this.notes.length + 1;
        note.createdAt = new Date();
        note.updatedAt = new Date();
        this.notes.push(note);
        return note;
    }

    findAll(): Note[] {
        return this.notes;
    }

    findOne(id: number): Note {
        return this.notes.find((note) => note.id === id);
    }

    update(id: number, updatedNote: Note): Note {
        const index = this.notes.findIndex((note) => note.id === id);
        if (index !== -1) {
            updatedNote.id = id;
            updatedNote.updatedAt = new Date();
            this.notes[index] = updatedNote;
            return updatedNote;
        }
        return null;
    }

    delete(id: number): Note {
        const index = this.notes.findIndex((note) => note.id === id);
        if (index !== -1) {
            const deletedNote = this.notes[index];
            this.notes.splice(index, 1);
            return deletedNote;
        }
        return null;
    }
}
```

[Up](../index.md)
[Main](../../../../index.md)
