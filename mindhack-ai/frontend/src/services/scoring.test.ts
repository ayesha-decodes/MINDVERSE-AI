import { describe, expect, it } from 'vitest';
import { accuracy, median } from './scoring';
describe('scoring helpers',()=>{
 it('calculates odd and even medians',()=>{expect(median([7,1,5])).toBe(5);expect(median([8,2,4,6])).toBe(5)});
 it('returns null for empty median',()=>expect(median([])).toBeNull());
 it('calculates accuracy safely',()=>{expect(accuracy(3,4)).toBe(75);expect(accuracy(0,0)).toBeNull()});
});
