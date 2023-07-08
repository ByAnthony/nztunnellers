/* eslint-disable max-len */
import { today } from '../../utils/date-utils';
import { Footer } from '../Footer/Footer';
import { Menu } from '../Menu/Menu';
import STYLES from './History.module.scss';

export function JourneyToWar() {
  return (
    <div>
      <Menu />
      <div className={STYLES.container}>
        <div className={STYLES.link}>
          <a href="/history">History</a>
          <span>/</span>
        </div>
        <div className={STYLES['chapter-title']}>
          <h1>
            <span className={STYLES['sub-title']}>Journey</span>
            <span className={STYLES.title}>To War</span>
          </h1>
          <div className={STYLES['chapter-number']}>2</div>
        </div>
        <div className={STYLES['image-container']}>
          <img
            className={STYLES.image}
            src="/images/history/FL13592442.jpg"
            alt="The Tunnellers were transported to Europe on the Steam Ship Ruapehu"
          />
        </div>
        <div className={STYLES.article}>
          <div className={STYLES.paragraph}>
            <h2>The Departure Day</h2>
            <p>
              On the morning of the 18&nbsp;December 1915 men packed their kit-bags and gathered in ranks on
              the Avondale racecourse. They all wore the khaki uniform and the official hat, which is special
              to the Engineers, ornamented with the &ldquo;puggaree&rdquo;, a three-line headband, two khaki
              lines encircling a third blue one, and the New Zealand Engineers badge with the motto: &ldquo;
              <em>Quo fas et gloria ducunt </em>
              – Where Duty and Glory Lead&rdquo;.
            </p>
            <p>
              The training was not still over and men were not yet complete soldiers. Their formation was
              going to continue during the travel
              <a href="#footnote_1" id="reference_1">[1]</a>
              . The Tunnellers walked to the port of Auckland where the Steam Ship
              <em> Ruapehu </em>
              was waiting for them. After putting their kit-bags on board, they were allowed to enjoy a meager
              lunch. Indeed cooks were on strike to protest against the unbearable rhythm of military transport
              <a href="#footnote_2" id="reference_2">[2]</a>
              .
            </p>
            <p>
              The Tunnellers had a very early breakfast and the only meal they could now have was composed
              of old biscuits and cheese. So it was a hungry Company that it went down to the quay and parade
              through the town to the statue of Sir George Grey located at the intersection of Queen Street
              and Grey’s Avenue
              <a href="#footnote_3" id="reference_3">[3]</a>
              . At that precise spot,
              James Allen, the Minister of Defence, and Christopher Parr, the Mayor of Auckland, delivered
              speeches in front of the troops and population. But the Tunnellers only thought of their empty
              stomachs.
            </p>
            <p>
              Then the Tunnellers started walking back to the port. On the way, families, friends and people
              warmly encouraged them
              <a href="#footnote_4" id="reference_4">[4]</a>
              . The night was
              already there when the Tunnellers were back on board. The men were happy to know that the strike
              was over and everything was back to normal for the journey. The
              {' '}
              <em>Ruapehu</em>
              {' '}
              was about to
              start its long travel towards Europe and it slowly sailed into the Pacific Ocean.
            </p>
          </div>
          <div className={STYLES['image-container']}>
            <img
              className={STYLES.image}
              src="/images/history/5200.jpg"
              alt="The New Zealand Tunnellers standing at the intersection of Queen Street and Grey’s Avenue"
            />
          </div>
          <div className={STYLES['image-legend']}>
            <div className={STYLES.title}>Last parade in Auckland</div>
            <div className={STYLES.captions}>Photographed by Lieutenant Robert H.P. Ronayne NZE</div>
            <div className={STYLES.reference}>MS 2008/45, Auckland War Memorial Museum</div>
          </div>
          <div className={STYLES.paragraph}>
            <h2>Around The Globe</h2>
            <p>
              After the Cap Horn, the southern point of the American continent, the
              <em> Ruapehu </em>
              headed to the port of Montevideo in Uruguay to halt there on 8&nbsp;January 1916. Uruguay being
              neutral, the New Zealand Tunnellers were not allowed to land there. The seamen of the
              <em> Ruapehu </em>
              were only authorized to load coal for the boat.
            </p>
            <p>
              The ship sailed next from Montevideo to Dakar, in Senegal, on the western coast of Africa. Life
              on the
              <em> Ruapehu </em>
              was quiet but a training programme was established from the beginning and followed until the end
              of the journey
              <a href="#footnote_5" id="reference_5">[5]</a>
              . Every day, to keep their shape, the men had to do some gymnastic and muscles-development exercises
              on the deck. Cultural activities were also provided to them. When they crossed the Equator, most of
              the men enjoyed the famous Equator baptism.
            </p>
            <p>
              In Dakar, Major Duigan succeeded to have the French authorities&apos; permission to disembark his
              Tunnellers and to walk with them in town as long as they did not bring any trouble. The Tunnellers
              had not disembarked for a month. They quickly shew friendliness singing and entertaining the population
              <a href="#footnote_6" id="reference_6">[6]</a>
              . The Senegalese soldiers welcomed them in striking up a vigorous &ldquo;Marseillaise&rdquo;, the
              French national anthem. Before embarking, the Tunnellers entertained the onlookers for the last time
              showing them the traditional Māori war dance: the &ldquo;haka&rdquo;.
            </p>
            <p>
              A 4.7&nbsp;naval gun had set up on the deck of the
              <em> Ruapehu </em>
              and gunners were on board to shoot if necessary. Indeed, when leaving Dakar, the ship entered the war
              zone and all the crew and men have been informed to be prepared for all eventualities
              <a href="#footnote_7" id="reference_7">[7]</a>
              . Some German submarines have been seen along the Moroccan and Portuguese coasts. They have already
              captured and sunk several Allies ships. But the end of the journey was uneventful and the
              <em> Ruapehu </em>
              entered the port of Plymouth, along Great Britain on 3&nbsp;February 1916.
            </p>
          </div>
          <div className={STYLES['image-container']}>
            <img
              className={STYLES.image}
              src="/images/history/bapteme.jpg"
              alt="The New Zealand Tunnellers standing at the intersection of Queen Street and Grey’s Avenue"
            />
          </div>
          <div className={STYLES['image-legend']}>
            <div className={STYLES.title}>The Equator baptism</div>
            <div className={STYLES.captions}>Photographed by Lieutenant Robert H.P. Ronayne NZE</div>
            <div className={STYLES.reference}>MS 2008/45, Auckland War Memorial Museum</div>
          </div>
          <div className={STYLES.paragraph}>
            <h2>Towards The Front Line</h2>
            <p>
              The Company immediately disembarked. The Tunnellers were going to start again their military training
              in better conditions than on the deck of the
              <em> Ruapehu </em>
              . All the men were gathered in a train heading to Falmouth where the population welcomed them with a
              banquet
              <a href="#footnote_8" id="reference_8">[8]</a>
              . After the meal, the Company walked through the town to reach the camp of Hornwork located on a
              headland and surrounded by the Castel of Pendennis.
            </p>
            <p>
              In a month, the Tunnellers had a very light formation to the underground warfare. Their training was
              again composed of knowing how to shoot with a gun, how to fight with a bayonet and walking for hours
              <a href="#footnote_9" id="reference_9">[9]</a>
              . On 7&nbsp;March 1916, all the kit-bags were ready; the men could be ready to embark for France.
              The population gathered for hard and moving farewell. One officer and 69&nbsp;men stayed in Falmouth
              as reinforcements, and then they moved to the New Zealand Depot in Hornchurch.
            </p>
            <p>
              The Company was transferred to Southampton and embarked on a ferry on 9&nbsp;March at 5pm. The men
              spent a cold night on the Channel and only reached Le Havre, in Normandy, at midnight. The New Zealand
              Engineers Tunneling Company became the first New Zealand unit to join the Western Front.
            </p>
            <p>
              In Le Havre, a group composed of one officer and 25&nbsp;men left the Company and joined the camp of
              the Royal Engineers settled in Rouen as another reinforcements. The unit took the train at 7am on
              11&nbsp;March and arrived on the next day at 6.30am at the railway station of Tincques, in Pas-de-Calais.
              Until 14&nbsp;March, men were billeted in the barns of Chelers, a nearby village. They waited for their
              transfer to the front line.
            </p>
            <p>
              On 15&nbsp;March, the New Zealand Tunnellers made their first steps in the trenches of the
              &ldquo;Labyrinth&rdquo; sector, located 3&nbsp;miles north of Arras, between the villages of Écurie and
              Roclincourt. They relieved the French sappers of the
              <em> 7/1&nbsp;compagnie d&apos;ingénieurs territoriaux</em>
              <a href="#footnote_10" id="reference_10">[10]</a>
              . After crossing the world, the Tunnellers were finally able to start their secret mission.
            </p>
          </div>
          <div className={STYLES['button-chapter-container']}>
            <a href="/history/journey-to-war" className={STYLES['button-chapter']} aria-label="Open the World War I timeline">
              <div>
                <p>Chapter 3</p>
                <span>Beneath Artois Fields</span>
              </div>
              <div className={STYLES.arrow}>&rarr;</div>
            </a>
          </div>
          <div className={STYLES.notes}>
            <h3>Notes</h3>
            <p>
              <a href="#reference_1" id="footnote_1">1.</a>
              {' '}
              Anthony BYLEDBAL,
              {' '}
              <em>Les Soldats fantômes de la Grande Guerre souterraine, 1915-1919. De l&apos;Immigrant p&#0257;keh&#0257; au vétéran oublié : les hommes de la New Zealand Engineers Tunnelling Company</em>
              , Doctoral thesis, under the supervision of Sophie-Anne Leterrier (University of Artois) and in collaboration with Nathalie Philippe (University of Waikato), University of Artois, 2012, p.&nbsp;197-227.
            </p>
            <p id="footnote_2">
              <a href="#reference_2">2.</a>
              {' '}
              James Campbell NEILL,
              {' '}
              <em>The New Zealand Tunnelling Company, 1915-1919</em>
              , Auckland, Whitcombe &amp; Tombs, 1922, p.&nbsp;10.
            </p>
            <p id="footnote_3">
              <a href="#reference_3">3.</a>
              {' '}
              <em>Ibid.</em>
            </p>
            <p id="footnote_4">
              <a href="#reference_4">4.</a>
              {' '}
              <em>Evening Post</em>
              , 20&nbsp;December 1915, p. 2, &ldquo;The Tunnelling Company marched through the streets yesterday. The appearance of the men made a very favourable impression upon the crowd in the street.&rdquo;
            </p>
            <p id="footnote_5">
              <a href="#reference_5">5.</a>
              {' '}
              Anthony BYLEDBAL,
              {' '}
              <em>Les Soldats fantômes de la Grande Guerre souterraine</em>
              ,
              {' '}
              <em>op. cit.</em>
              , p.&nbsp;1147-1153.
            </p>
            <p id="footnote_6">
              <a href="#reference_6">6.</a>
              {' '}
              James Campbell NEILL,
              {' '}
              <em>The New Zealand Tunnelling Company&hellip;</em>
              ,
              {' '}
              <em>op. cit.</em>
              , p.&nbsp;14.
            </p>
            <p id="footnote_7">
              <a href="#reference_7">7.</a>
              {' '}
              <em>Ibid.</em>
              , p.&nbsp;13, &ldquo;From Monte Video she made a direct run to Dakar in French Senegambia to ship a 4.7&nbsp;naval gun and gunners for defence from submarines &rdquo;.
            </p>
            <p id="footnote_8">
              <a href="#reference_8">8.</a>
              {' '}
              <em>Ibid.</em>
              , p.&nbsp;14, &ldquo;a truly sumptuous repast … served by all the youth and beauty of that ancient town.&rdquo;
            </p>
            <p id="footnote_9">
              <a href="#reference_9">9.</a>
              {' '}
              Anthony BYLEDBAL,
              {' '}
              <em>Les Soldats fantômes de la Grande Guerre souterraine</em>
              ,
              {' '}
              <em>op. cit.</em>
              , p.&nbsp;258.
            </p>
            <p id="footnote_10">
              <a href="#reference_10">10.</a>
              {' '}
              The National Archives United Kingdom, WO 95/407, War Diary of the New Zealand Engineers Tunnelling Company, 15&nbsp;March 1916.
            </p>
          </div>
          <div className={STYLES.notes}>
            <h3>How to cite this page</h3>
            <p>
              Anthony Byledbal, &ldquo;Call To Pick & Shovel&rdquo;,
              {' '}
              <em>New Zealand Tunnellers Website</em>
              ,
              {' '}
              {`${today.getFullYear()}`}
              {' '}
              (2009),
              Accessed:
              {' '}
              {`${today.toLocaleDateString('en-NZ', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
              })}. `}
            </p>
          </div>
        </div>
        <Footer />
      </div>
    </div>
  );
}
