import type { NextPage } from 'next'
import styles from '../styles/Home.module.css'
import algoliasearch from 'algoliasearch/lite';
import { InstantSearch, SearchBox, Hits } from 'react-instantsearch-dom';

const searchClient = algoliasearch(
  'latency',
  '6be0576ff61c053d5f9a3225e2a90f76'
);

const Home: NextPage = () => {
  return (
    <div>
      <h1>DigiDirectory</h1>
      <InstantSearch searchClient={searchClient} indexName="demo_ecommerce">
        <SearchBox />
        <Hits />
      </InstantSearch>
    </div>
  )
}

export default Home
