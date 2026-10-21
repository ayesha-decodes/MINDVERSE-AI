import { describe, expect, it } from 'vitest';
import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import App, { getGameAdvice } from './App';
describe('MindVerse home',()=>{it('renders the hero and navigation',()=>{render(<BrowserRouter><App/></BrowserRouter>);expect(screen.getByText(/Ever wondered how your brain/i)).toBeInTheDocument();expect(screen.getByText('The games')).toBeInTheDocument();})});
describe('game advice',()=>{it('returns a helpful tip for each completed game',()=>{expect(getGameAdvice('reaction', 90)).toMatch(/reaction|quick|signal/i);expect(getGameAdvice('memory', 70)).toMatch(/memory|sequence|pattern/i);expect(getGameAdvice('focus', 60)).toMatch(/focus|attention|color/i);expect(getGameAdvice('motion', 80)).toMatch(/motion|hand|coordination/i);expect(getGameAdvice('gaze', 75)).toMatch(/gaze|visual|scan/i);})});
