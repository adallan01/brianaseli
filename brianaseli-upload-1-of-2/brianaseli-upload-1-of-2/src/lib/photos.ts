import type { ImageMetadata } from 'astro';
import blackTee from '../assets/photos/portrait-black-tee.jpg';
import thinking from '../assets/photos/portrait-thinking.jpg';
import laugh from '../assets/photos/portrait-laugh.jpg';
import smile from '../assets/photos/portrait-smile.jpg';
import frameHands from '../assets/photos/frame-hands.jpg';
import eventNight from '../assets/photos/event-night.jpg';
import leather from '../assets/photos/portrait-leather.jpg';
import stageMic from '../assets/photos/stage-mic.jpg';
import suit from '../assets/photos/portrait-suit.jpg';

import cutThinking from '../assets/cutouts/brian-thinking.png';
import cutLeather from '../assets/cutouts/brian-leather.png';
import cutBlackTee from '../assets/cutouts/brian-blacktee.png';
import cutSuit from '../assets/cutouts/brian-suit.png';

import spotlight from '../assets/stage/spotlight.jpg';
import brick from '../assets/stage/brick.jpg';
import sparkle from '../assets/stage/sparkle.jpg';
import podium from '../assets/stage/podium.jpg';
import hexsphere from '../assets/stage/hexsphere.jpg';
import silhouettes from '../assets/stage/silhouettes.jpg';
import eventHall from '../assets/stage/event-hall.jpg';
import gala from '../assets/stage/gala.jpg';

/** Real photographs of Brian. `pos` is the focal point used for object-position on any crop. */
export const photos = {
  'portrait-black-tee': { src: blackTee, alt: 'Brian Aseli smiling broadly in a black T-shirt', pos: '50% 30%' },
  'portrait-thinking': { src: thinking, alt: 'Brian Aseli smiling with his hand at his chin', pos: '50% 22%' },
  'portrait-laugh': { src: laugh, alt: 'Brian Aseli laughing, hand at his chin', pos: '50% 35%' },
  'portrait-smile': { src: smile, alt: 'Brian Aseli smiling in a white T-shirt', pos: '50% 30%' },
  'frame-hands': { src: frameHands, alt: 'Brian Aseli framing the camera with both hands', pos: '50% 30%' },
  'event-night': { src: eventNight, alt: 'Brian Aseli at an evening event in Nairobi, arms crossed, wearing beaded wrist cuffs', pos: '58% 35%' },
  'portrait-leather': { src: leather, alt: 'Brian Aseli in a leather jacket and round sunglasses, laughing', pos: '50% 25%' },
  'stage-mic': { src: stageMic, alt: 'Brian Aseli on stage with a microphone, in a sequinned jacket', pos: '50% 25%' },
  'portrait-suit': { src: suit, alt: 'Brian Aseli seated in an armchair in a dark green suit', pos: '50% 20%' },
} as const;
export type PhotoKey = keyof typeof photos;

/** Brian with the studio background removed, for placing under stage light. */
export const cutouts = {
  thinking: { src: cutThinking, alt: 'Brian Aseli, smiling, hand at his chin' },
  leather: { src: cutLeather, alt: 'Brian Aseli in a leather jacket and sunglasses, laughing' },
  blacktee: { src: cutBlackTee, alt: 'Brian Aseli smiling in a black T-shirt' },
  suit: { src: cutSuit, alt: 'Brian Aseli seated in an armchair in a dark green suit' },
} as const;
export type CutoutKey = keyof typeof cutouts;

/** Atmospheric stage backgrounds, graded to the brand blue (decorative, empty alt). */
export const stages = { spotlight, brick, sparkle, podium, hexsphere, silhouettes, 'event-hall': eventHall, gala } as const;
export type StageKey = keyof typeof stages;
/** Where the light is in each background, for object-position. */
export const stagePos: Record<StageKey, string> = { spotlight: '50% 20%', brick: '50% 15%', sparkle: '50% 20%', podium: '50% 30%', hexsphere: '50% 40%', silhouettes: '50% 70%', 'event-hall': '50% 45%', gala: '50% 88%' };

const fromGlob = (g: Record<string, { default: ImageMetadata }>, prefix = '') =>
  Object.fromEntries(Object.entries(g).map(([k, v]) => [k.split('/').pop()!.replace(/\.jpg$/, '').replace(prefix, ''), v.default]));

/** YouTube thumbnails saved locally, keyed by video id. */
export const thumbs = fromGlob(import.meta.glob('../assets/thumbs/*.jpg', { eager: true }));
/** Event photos, keyed by file name. */
export const events = fromGlob(import.meta.glob('../assets/events/*.jpg', { eager: true }));
/** Brand-blue duotone versions of photos, thumbs ("thumb-<id>") and events ("event-<name>"). */
export const duo = fromGlob(import.meta.glob('../assets/duo/*.jpg', { eager: true }));
