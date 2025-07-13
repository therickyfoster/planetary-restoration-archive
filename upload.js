import { NFTStorage } from 'nft.storage';
import { filesFromPaths } from 'files-from-path';
import { globby } from 'globby';
import path from 'path';

async function main() {
  const paths = await globby([
    'innovations/**',
    '!innovations',
    '!innovations/**/.DS_Store'
  ]);

  const files = await filesFromPaths(paths);

  console.log(`📦 Uploading ${files.length} files...`);

  const client = new NFTStorage({ token: process.env.NFT_STORAGE_API_TOKEN });
  const cid = await client.storeDirectory(files);

  console.log('✅ Uploaded folder with CID:', cid);
  console.log(`🔗 IPFS URL: https://nftstorage.link/ipfs/${cid}`);
}

main().catch(err => {
  console.error('❌ Upload failed:', err.message || err);
  console.error(err.stack);
  process.exit(1);
});
